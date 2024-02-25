from typing import Callable

import tensorflow as tf
from omegaconf import DictConfig


def generate_model(config: DictConfig, top_model: Callable):

    fe = tf.keras.applications.EfficientNetB0(
        include_top=False, weights="imagenet", input_shape=(224, 224, 3)
    )

    for layer in fe.layers:
        layer.trainable = True

    gap = tf.keras.layers.GlobalAveragePooling2D()(fe.output)

    top_model = top_model(gap)

    model = tf.keras.models.Model(inputs=fe.input, outputs=top_model)
    return model
