import os
from pathlib import Path

import tensorflow as tf
from omegaconf import DictConfig


def evaluate_model(
    config: DictConfig,
    current_datetime_strgfied,
    epoch_to_evaluate,
    test_dataset,
    custom_objects,
):
    """Function to evaluate the model"""

    project_root_path = Path(os.getcwd())

    # extract the initial chars of the model checkpoint filename
    model_filename = config.model_training.model_checkpoint_filename.split(".")[
        0
    ].format(epoch=epoch_to_evaluate)

    # iterate over the available checkpoints to select the correct model
    model_path = (
        f"{project_root_path}/{config.model_training.checkpoint_root_path}/"
        f"{current_datetime_strgfied}/{model_filename}"
    )

    print(f"Found {model_path}. Loading and evaluating it...")
    model = tf.keras.models.load_model(
        model_path,
        custom_objects=custom_objects,
    )
    model_evaluation_result = model.evaluate(test_dataset)

    return model, model_evaluation_result
