import os
from functools import partial
from pathlib import Path
from typing import Callable, Iterable

import pandas as pd
import tensorflow as tf
from omegaconf import DictConfig

from car_azimuth_predictor.utils.training_tools import (
    CustomHorizontalFlip,
    augment_image,
    prepare_input,
    preprocess_image,
)


def generate_datasets(
    config: DictConfig,
    gt_cols: Iterable[str],
    pose_flip_fn: Callable,
    batch_size: int,
    augment: bool,
):
    """Function to adjust prediction values"""

    root_path = Path(os.getcwd())

    df_path = root_path / config.dataset_generation.df_path
    # df_train_path = root_path / config.dataset_generation.df_train_path
    # df_val_path = root_path / config.dataset_generation.df_val_path
    # df_test_path = root_path / config.dataset_generation.df_test_path

    df = pd.read_csv(df_path)
    df_train = df[df["is_train"] == 1]
    df_val = df[df["is_train"] == 0]

    train_dataset = tf.data.Dataset.from_tensor_slices(
        (df_train["image_path"], df_train[gt_cols])
    )
    val_dataset = tf.data.Dataset.from_tensor_slices(
        (df_val["image_path"], df_val[gt_cols])
    )

    train_dataset = train_dataset.shuffle(df_train.shape[0])

    image_size = (
        config.dataset_generation.image_height,
        config.dataset_generation.image_width,
    )

    prepare_input_partial = partial(prepare_input, image_size=image_size)
    train_dataset = train_dataset.map(
        prepare_input_partial,
        num_parallel_calls=tf.data.AUTOTUNE,
    )

    if augment:
        custom_horizontal_flip = CustomHorizontalFlip(pose_flip_fn)
        augment_image_partial = partial(
            augment_image, custom_horizontal_flip=custom_horizontal_flip
        )
        train_dataset = train_dataset.map(
            augment_image_partial, num_parallel_calls=tf.data.AUTOTUNE
        )

    train_dataset = (
        train_dataset.map(preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)
        .batch(batch_size, drop_remainder=True)
        .prefetch(tf.data.AUTOTUNE)
    )

    val_dataset = (
        val_dataset.map(
            prepare_input_partial,
            num_parallel_calls=tf.data.AUTOTUNE,
        )
        .map(preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)
        .batch(batch_size, drop_remainder=False)
        .prefetch(tf.data.AUTOTUNE)
    )


    return train_dataset, val_dataset
