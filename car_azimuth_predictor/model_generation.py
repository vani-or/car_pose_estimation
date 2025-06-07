from typing import Callable
import tensorflow as tf


def generate_model(head_model: Callable, model_backbone_name: str = "efficientnet"):

    if model_backbone_name == "efficientnet":
        fe = tf.keras.applications.EfficientNetB0(
            include_top=False, weights="imagenet", input_shape=(224, 224, 3)
        )
    elif model_backbone_name == "mobilenet":
        fe = tf.keras.applications.MobileNetV3Small(
            include_top=False, weights="imagenet", input_shape=(224, 224, 3)
        )
    else:
        raise ValueError(f"Unsupported model backbone: {model_backbone_name}")

    for layer in fe.layers:
        layer.trainable = True

    gap = tf.keras.layers.GlobalAveragePooling2D()(fe.output)

    head_model = head_model(gap)

    model = tf.keras.models.Model(inputs=fe.input, outputs=head_model)
    return model
