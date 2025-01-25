import json
import os
import tempfile
import pickle
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
    save_model_path: str = None,
    train_history_path: str = None,
    epochs: int = 100,
    early_stopping_patience: int = 10,
    verbose: int = 1,
):
    """Function to train the model"""

    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    with tempfile.TemporaryDirectory() as tmpdirname:
        model_checkpoint_path = os.path.join(
            tmpdirname, f"model_checkpoint_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        )

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            model_checkpoint_path, save_best_only=True, monitor="val_loss"
        )

        es_callback = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            min_delta=0.0,
            patience=early_stopping_patience,
            verbose=verbose,
            mode="min",
            baseline=None,
            restore_best_weights=True,
        )

        train_history = model.fit(
            train_dataset,
            epochs=epochs,
            use_multiprocessing=True,
            callbacks=[checkpoint_callback, es_callback],
            validation_data=validation_dataset,
            verbose=verbose,
        )

        if save_model_path is not None:
            model.save(save_model_path)

    if train_history_path is not None:
        with open(train_history_path, "wb") as fp:
            pickle.dump(train_history, fp)

    return train_history
