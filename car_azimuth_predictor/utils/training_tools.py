import random
from typing import Callable

import albumentations as A
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from albumentations.augmentations import functional as F
from tensorflow.keras.applications.efficientnet_v2 import (
    preprocess_input as preprocess_input_effnet,
)


def tf_align_pred_angle(y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor) -> tf.Tensor:
    positive_cond = tf.cast(y_true_angle - y_pred_angle > np.pi, tf.float32)
    negative_cond = tf.cast(y_true_angle - y_pred_angle < -np.pi, tf.float32)

    y_pred_angle += positive_cond * np.pi * 2
    y_pred_angle -= negative_cond * np.pi * 2

    return y_pred_angle


def tf_mean_absolute_angle_error(
    y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor
) -> tf.Tensor:
    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    return tf.math.reduce_mean(tf.math.abs(y_true_angle - y_pred_angle)) / np.pi * 180


def tf_mean_absolute_angle_error_sin_cos_output(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf.math.atan2(y_true[:, 0], y_true[:, 1])
    y_pred_angle = tf.math.atan2(y_pred[:, 0], y_pred[:, 1])

    return tf_mean_absolute_angle_error(y_true_angle, y_pred_angle)


def tf_median_absolute_angle_error(
    y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor
) -> tf.Tensor:
    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    return (
        tfp.stats.percentile(
            tf.math.abs(y_true_angle - y_pred_angle), 50, interpolation="midpoint"
        )
        / np.pi
        * 180
    )


def tf_median_absolute_angle_error_sin_cos_output(y_true: tf.Tensor, y_pred: tf.Tensor):
    y_true_angle = tf.math.atan2(y_true[:, 0], y_true[:, 1])
    y_pred_angle = tf.math.atan2(y_pred[:, 0], y_pred[:, 1])

    return tf_median_absolute_angle_error(y_true_angle, y_pred_angle)


def tf_acc_pi_6(y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor) -> tf.Tensor:
    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    positive = tf.cast(tf.math.abs(y_true_angle - y_pred_angle) < np.pi / 6, tf.float32)

    return tf.reduce_mean(positive)


def tf_acc_pi_6_sin_cos_output(y_true: tf.Tensor, y_pred: tf.Tensor):
    y_true_angle = tf.math.atan2(y_true[:, 0], y_true[:, 1])
    y_pred_angle = tf.math.atan2(y_pred[:, 0], y_pred[:, 1])

    return tf_acc_pi_6(y_true_angle, y_pred_angle)


def tf_rmse_angle(y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor) -> tf.Tensor:
    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    return (
        tf.math.sqrt(tf.math.reduce_mean(tf.math.square(y_pred_angle - y_true_angle)))
        * 180
        / np.pi
    )


def tf_rmse_angle_sin_cos_output(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    y_true_angle = tf.math.atan2(y_true[:, 0], y_true[:, 1])
    y_pred_angle = tf.math.atan2(y_pred[:, 0], y_pred[:, 1])

    return tf_rmse_angle(y_true_angle, y_pred_angle)


def tf_r2_angle_score(y_true_angle: tf.Tensor, y_pred_angle: tf.Tensor) -> tf.Tensor:
    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    y_true_mean = tf.math.reduce_mean(y_true_angle)

    return 1 - tf.math.reduce_sum(
        tf.math.pow(y_true_angle - y_pred_angle, 2)
    ) / tf.math.reduce_sum(tf.math.pow(y_true_angle - y_true_mean, 2))


def tf_r2_angle_score_sin_cos_output(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    y_true_angle = tf.math.atan2(y_true[:, 0], y_true[:, 1])
    y_pred_angle = tf.math.atan2(y_pred[:, 0], y_pred[:, 1])

    return tf_r2_angle_score(y_true_angle, y_pred_angle)


def tf_get_angle_from_double_sigmoids(y_output: tf.Tensor) -> tf.Tensor:
    y_pred_abs_angle = y_output * np.pi

    # First we need to get the quadrant from 2 angles of the y_output,
    # both are positive numbers from 0 to PI, but the second one's zero is aligned to PI/2
    alfa_less_90 = y_pred_abs_angle[:, 0] < np.pi / 2
    beta_less_90 = y_pred_abs_angle[:, 1] < np.pi / 2
    quad1_cond = alfa_less_90 & beta_less_90
    quad2_cond = ~alfa_less_90 & beta_less_90
    quad3_cond = ~alfa_less_90 & ~beta_less_90
    quad4_cond = alfa_less_90 & ~beta_less_90

    # Then knowing the correct quadrant we define alfa2 from the beta angle which is aligned to original alfa
    alfa2_from_beta = 0
    alfa2_from_beta += tf.cast(quad1_cond, tf.float32) * (
        np.pi / 2 - y_pred_abs_angle[:, 1]
    )
    alfa2_from_beta += tf.cast(quad2_cond, tf.float32) * (
        np.pi / 2 + y_pred_abs_angle[:, 1]
    )
    alfa2_from_beta += tf.cast(quad3_cond, tf.float32) * (
        3 * np.pi / 2 - y_pred_abs_angle[:, 1]
    )
    alfa2_from_beta += tf.cast(quad4_cond, tf.float32) * (
        -np.pi / 2 + y_pred_abs_angle[:, 1]
    )

    # Knowing two angles and the quadrant of the target we revover the real position of the azimuth
    mean_alfa_angle = (y_pred_abs_angle[:, 0] + alfa2_from_beta) / 2
    mean_alfa_angle *= -1 * (tf.cast(quad3_cond | quad4_cond, tf.float32) * 2 - 1)
    return mean_alfa_angle


def np_get_angle_from_double_sigmoids(y_sigmoids: np.ndarray) -> np.ndarray:
    """
    Numpy implementation of tf_get_angle_from_double_sigmoids

    Parameters
    ----------
    y_sigmoids

    Returns
    -------

    """
    assert len(y_sigmoids.shape) > 1, f"shape is {y_sigmoids.shape}"
    # print(y_sigmoids)
    y_pred_abs_angle = y_sigmoids * np.pi

    alfa_less_90 = y_pred_abs_angle[:, 0] < np.pi / 2
    beta_less_90 = y_pred_abs_angle[:, 1] < np.pi / 2
    quad1_cond = alfa_less_90 * beta_less_90
    quad2_cond = (1 - alfa_less_90) * beta_less_90
    quad3_cond = (1 - alfa_less_90) * (1 - beta_less_90)
    quad4_cond = alfa_less_90 * (1 - beta_less_90)

    alfa2_from_beta = 0
    alfa2_from_beta += quad1_cond * (np.pi / 2 - y_pred_abs_angle[:, 1])
    alfa2_from_beta += quad2_cond * (np.pi / 2 + y_pred_abs_angle[:, 1])
    alfa2_from_beta += quad3_cond * (3 * np.pi / 2 - y_pred_abs_angle[:, 1])
    alfa2_from_beta += quad4_cond * (-np.pi / 2 + y_pred_abs_angle[:, 1])

    # TODO: reallign ?
    mean_alfa_angle = (y_pred_abs_angle[:, 0] + alfa2_from_beta) / 2
    mean_alfa_angle *= -1 * ((quad3_cond + quad4_cond) * 2 - 1)

    return mean_alfa_angle


def tf_get_angle_from_double_sigmoids_old(y_output: tf.Tensor) -> tf.Tensor:
    y_pred_abs_angle = y_output[:, 0] * np.pi
    sign_cond = tf.cast(y_output[:, 1] < 0.5, tf.float32) * 2 - 1
    return sign_cond * y_pred_abs_angle


def np_get_angle_from_double_sigmoids_old(y_sigmoids: np.ndarray) -> np.ndarray:
    y_pred_abs_angle = y_sigmoids[:, 0] * np.pi
    sign_cond = (y_sigmoids[:, 1] < 0.5) * 2 - 1
    return sign_cond * y_pred_abs_angle  # TODO: not tested, but should be correct


def np_get_sigmoids_from_angle(angle_radians: np.ndarray) -> np.ndarray:
    cond = angle_radians > np.pi
    first_sigm = angle_radians - cond * 2 * np.pi

    shifted_radians = angle_radians - np.pi / 2
    cond = shifted_radians > np.pi
    second_sigm = shifted_radians - cond * 2 * np.pi

    return np.stack(first_sigm, second_sigm)  # TODO: not tested even once


def np_get_angle_from_sin_cos(y_sincos: np.ndarray) -> np.ndarray:
    return np.arctan2(y_sincos[:, 0], y_sincos[:, 1])


def tf_mean_absolute_angle_error_double_sigmoid(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids(y_pred)

    return tf_mean_absolute_angle_error(y_true_angle, y_pred_angle)


def tf_median_absolute_angle_error_double_sigmoid(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids(y_pred)

    return tf_median_absolute_angle_error(y_true_angle, y_pred_angle)


def tf_acc_pi_6_double_sigmoid(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids(y_pred)

    return tf_acc_pi_6(y_true_angle, y_pred_angle)


def tf_mean_absolute_angle_error_double_sigmoid_old(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids_old(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids_old(y_pred)

    return tf_mean_absolute_angle_error(y_true_angle, y_pred_angle)


def tf_r2_angle_score_double_sigmoid(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids(y_pred)

    return tf_r2_angle_score(y_true_angle, y_pred_angle)


def tf_r2_angle_score_double_sigmoid_old(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids_old(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids_old(y_pred)

    return tf_r2_angle_score(y_true_angle, y_pred_angle)


def tf_rmse_angle_score_double_sigmoid(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids(y_pred)

    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    return (
        tf.math.sqrt(tf.math.reduce_mean(tf.math.square(y_pred_angle - y_true_angle)))
        / np.pi
        * 180
    )


def tf_rmse_angle_score_double_sigmoid_old(
    y_true: tf.Tensor, y_pred: tf.Tensor
) -> tf.Tensor:
    y_true_angle = tf_get_angle_from_double_sigmoids_old(y_true)
    y_pred_angle = tf_get_angle_from_double_sigmoids_old(y_pred)

    y_pred_angle = tf_align_pred_angle(y_true_angle, y_pred_angle)

    return (
        tf.math.sqrt(tf.math.reduce_mean(tf.math.square(y_pred_angle - y_true_angle)))
        / np.pi
        * 180
    )


def np_shift_05_pi(orig_radians: np.ndarray) -> np.ndarray:
    shifted_radians = orig_radians - 0.5 * np.pi
    shifted_radians -= (shifted_radians >= np.pi) * 2 * np.pi
    shifted_radians += (shifted_radians < -np.pi) * 2 * np.pi
    return shifted_radians


transforms = A.Compose(
    [
        A.Rotate(limit=10, p=0.5),
        A.OpticalDistortion(distort_limit=(0, 0.2), p=0.7),
        A.RandomCrop(height=180, width=180, p=0.5),
        A.RandomBrightnessContrast(brightness_limit=0.15, contrast_limit=0.15, p=0.5),
        A.Resize(*(224, 224), always_apply=True),
    ]
)


def prepare_input(file_path, y_true, image_size):
    img = tf.io.read_file(file_path)

    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, image_size)

    return img, y_true


class CustomHorizontalFlip:
    def __init__(self, pose_flip_fn: Callable):
        self.pose_flip_fn = pose_flip_fn

    def __call__(self, img, pose, p):
        if random.random() < p:
            if img.ndim == 3 and img.shape[2] > 1 and img.dtype == np.uint8:
                # Opencv is faster than numpy only in case of
                # non-gray scale 8bits images
                return F.hflip_cv2(img)
            flipped_image = F.hflip(img)
            flipped_pose = self.pose_flip_fn(pose)
            return flipped_image, flipped_pose
        return img, pose


def horizontal_flip_pose_sin_cos_output(pose):
    return [-pose[0], pose[1]]


def horizontal_flip_pose_double_sigmoid(pose):
    return [pose[0], 1 - pose[1]]


def preprocess_image(img, y_true):
    img = preprocess_input_effnet(img)
    return img, y_true


def apply_transform(image):
    data = {"image": image}
    aug_data = transforms(**data)
    aug_img = aug_data["image"]
    return image, aug_img


def augment_image(img, y_true, custom_horizontal_flip: Callable):
    aug_img, aug_y = tf.numpy_function(
        func=custom_horizontal_flip,
        inp=[img, y_true, 0.5],
        Tout=[tf.float32, tf.double],
    )
    aug_img = tf.cast(aug_img, tf.uint8)
    img, aug_img = tf.numpy_function(
        func=apply_transform, inp=[aug_img], Tout=[tf.uint8, tf.uint8]
    )
    aug_img = tf.cast(aug_img, tf.float32)
    return aug_img, aug_y


def angle_double_output_loss(y_true, y_pred):
    angle_loss = tf.keras.metrics.binary_crossentropy(y_true[:, 0], y_pred[:, 0])
    angle2_loss = tf.keras.metrics.binary_crossentropy(y_true[:, 1], y_pred[:, 1])
    return angle_loss + angle2_loss
