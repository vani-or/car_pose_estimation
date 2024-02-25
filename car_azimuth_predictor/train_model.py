import json
import os
from datetime import datetime
from pathlib import Path
from typing import Iterable

import tensorflow as tf
from omegaconf import DictConfig


def train_model(
    config: DictConfig,
    model: tf.keras.Model,
    train_dataset: tf.data.Dataset,
    validation_dataset: tf.data.Dataset,
    optimizer: tf.keras.optimizers.Optimizer,
    loss: tf.keras.losses.Loss,
    metrics: Iterable,
    persist_history: bool = False,
    verbose: int = 1,
):
    """Function to train the model"""

    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    root_path = Path(os.getcwd())

    current_datetime_strgfied = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    model_temp_out = os.path.join(
        root_path,
        config.model_training.checkpoint_root_path,
        current_datetime_strgfied,
    )
    print(f"Saving models' checkpoints to {model_temp_out}")
    os.makedirs(model_temp_out, exist_ok=True)
    model_checkpoint_path = os.path.join(
        model_temp_out, config.model_training.model_checkpoint_filename
    )

    c1 = tf.keras.callbacks.ModelCheckpoint(
        model_checkpoint_path, save_best_only=True, monitor="val_loss"
    )

    # c2 = ReduceLRBacktrack(
    #     best_path=model_checkpoint_path,
    #     monitor="val_loss",
    #     factor=0.25,
    #     patience=3,
    #     min_delta=0.0,
    # )

    c3 = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        min_delta=0.0,
        patience=10,
        verbose=1,
        mode="min",
        baseline=None,
        restore_best_weights=True,
    )

    train_history = model.fit(
        train_dataset,
        epochs=100,
        use_multiprocessing=True,
        callbacks=[c1, c3],
        validation_data=validation_dataset,
        verbose=verbose,
    )

    if persist_history:
        with open(os.path.join(model_temp_out, "train_history.json"), "w") as fp:
            json.dump(train_history.history, fp)

    return train_history, current_datetime_strgfied
