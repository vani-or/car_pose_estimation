import argparse
from keras.models import load_model
import os
from PIL import Image
import tensorflow as tf
import numpy as np
import json

from car_azimuth_predictor.utils.visualization_tools import plot_image_from_path

import tensorflow_hub as hub
from car_azimuth_predictor.utils.training_tools import (
    horizontal_flip_pose_sin_cos_output,
    tf_acc_pi_6_sin_cos_output,
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
    # Approach 2
    angle_double_output_loss,
    horizontal_flip_pose_double_sigmoid,
    tf_mean_absolute_angle_error_double_sigmoid,
    tf_median_absolute_angle_error_double_sigmoid,
    tf_r2_angle_score_double_sigmoid,
    tf_rmse_angle_score_double_sigmoid,
    tf_acc_pi_6_double_sigmoid,
    np_get_angle_from_double_sigmoids,
    np_get_angle_from_sin_cos,
)


def load_image_to_tensor(image_path: str) -> tf.Tensor:
    """Allows you to load image to tensor.

    :param image_path:
    :return image_tensor:
    """
    image = Image.open(image_path).convert("RGB")
    image_tensor = tf.convert_to_tensor(np.array(image), dtype=tf.float32)
    image_tensor = tf.image.resize(image_tensor, (224, 224))

    return image_tensor


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def main(model_path, images_path, approach: str, batch_size=32, output_path=None, visualizations_path=None, units='degrees'):
    if approach == "1":
        azimuth_converter = np_get_angle_from_sin_cos
    elif approach == "2":
        azimuth_converter = np_get_angle_from_double_sigmoids
    else:
        raise ValueError("Unknown approach")

    model = load_model(model_path, custom_objects={
        "KerasLayer": hub.KerasLayer,
        "angle_double_output_loss": angle_double_output_loss,
        "tf_mean_absolute_angle_error_double_sigmoid": tf_mean_absolute_angle_error_double_sigmoid,
        "tf_rmse_angle_score_double_sigmoid": tf_rmse_angle_score_double_sigmoid,
        "tf_r2_angle_score_double_sigmoid": tf_r2_angle_score_double_sigmoid,
        "tf_median_absolute_angle_error_double_sigmoid": tf_median_absolute_angle_error_double_sigmoid,
        "tf_acc_pi_6_double_sigmoid": tf_acc_pi_6_double_sigmoid,
        "horizontal_flip_pose_double_sigmoid": horizontal_flip_pose_double_sigmoid,
        "tf_mean_absolute_angle_error_sin_cos_output": tf_mean_absolute_angle_error_sin_cos_output,
        "tf_rmse_angle_sin_cos_output": tf_rmse_angle_sin_cos_output,
        "tf_r2_angle_score_sin_cos_output": tf_r2_angle_score_sin_cos_output,
        "tf_median_absolute_angle_error_sin_cos_output": tf_median_absolute_angle_error_sin_cos_output,
        "tf_acc_pi_6_sin_cos_output": tf_acc_pi_6_sin_cos_output,
        "horizontal_flip_pose_sin_cos_output": horizontal_flip_pose_sin_cos_output,
    })

    all_predictions = []
    files = sorted(os.listdir(images_path))
    for image_path in chunker(files, batch_size):
        images = [load_image_to_tensor(os.path.join(images_path, image)) for image in image_path]
        images = tf.stack(images, axis=0)
        predictions = model.predict(images)
        all_predictions.extend(predictions)

    azimuths = azimuth_converter(np.array(all_predictions))
    if units == 'degrees':
        azimuths = azimuths / np.pi * 180
    elif units != 'radians':
        raise ValueError("Unknown units")

    azimuths = azimuths.astype(float).tolist()

    output = []
    for i, (image_path, azimuth) in enumerate(zip(files, azimuths)):
        output.append({"image": image_path, "azimuth": azimuth})
    with open(output_path, "w") as f:
        json.dump(output, f)

    if visualizations_path is not None:
        import matplotlib.pyplot as plt
        os.makedirs(visualizations_path, exist_ok=True)
        for i, (image_path, azimuth) in enumerate(zip(files, azimuths)):
            plot_image_from_path(os.path.join(images_path, image_path), azimuth, None)
            save_path = os.path.join(visualizations_path, os.path.basename(image_path))
            plt.tight_layout()
            plt.savefig(save_path)

    return azimuths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate a model')
    parser.add_argument('--model_path', type=str, help='Path to the model', required=True)
    parser.add_argument("--approach", type=str, help="Approach to use (1 = Sin/Cos, 2 = Directional discriminators)", choices=["1", "2"], required=True)
    parser.add_argument('--images_path', type=str, help='Path to the images', required=True)
    parser.add_argument('--output_path', type=str, help='Path to the output file', required=True)
    parser.add_argument('--visualizations_path', type=str, help='Path to the visualizations', default=None)
    parser.add_argument('--batch_size', type=int, help='Batch size', default=16)
    parser.add_argument('--units', type=str, help='Use radians or degrees', default='degrees', choices=['radians', 'degrees'])
    args = parser.parse_args()
    main(args.model_path, args.images_path, args.approach, args.batch_size, args.output_path, args.visualizations_path)
