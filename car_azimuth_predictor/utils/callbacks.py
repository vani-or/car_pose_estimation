import logging

import numpy as np
import tensorflow as tf
from tensorflow.keras import backend
from tensorflow.keras.callbacks import ReduceLROnPlateau


class CheckpointLR(ReduceLROnPlateau):
    """
    https://stackoverflow.com/a/52227664/1581927
    """

    def on_epoch_end(self, epoch, logs=None):
        if not self.in_cooldown():
            temp = self.model.get_weights()
            self.model.set_weights(self.last_weights)
            self.last_weights = temp
        super().on_epoch_end(epoch, logs)  # actually reduce LR


class ReduceLRBacktrack(ReduceLROnPlateau):
    """
    https://stackoverflow.com/a/55228619/1581927
    """

    def __init__(self, *args, **kwargs):
        super(ReduceLRBacktrack, self).__init__(*args, **kwargs)
        self.logger = tf.get_logger()
        self.best_weights = None
        self.best_monitor_value = None

    def on_train_begin(self, logs=None):
        # Allow instances to be re-used
        self.best_weights = None
        self.best_monitor_value = None

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        logs["lr"] = backend.get_value(self.model.optimizer.lr)
        current = logs.get(self.monitor)
        if current is None:
            logging.warning(
                "Learning rate reduction is conditioned on metric `%s` "
                "which is not available. Available metrics are: %s",
                self.monitor,
                ",".join(list(logs.keys())),
            )

        else:
            if self.in_cooldown():
                self.cooldown_counter -= 1
                self.wait = 0

            if self.monitor_op(current, self.best):
                self.best = current
                self.wait = 0
                self.best_weights = self.model.get_weights()
                logging.debug(f"Saving weights of the model... best={self.best}")

            elif not self.in_cooldown():
                self.wait += 1
                if self.wait >= self.patience:
                    old_lr = backend.get_value(self.model.optimizer.lr)
                    if old_lr > np.float32(self.min_lr):

                        # TODO: caricare i pesi dell'epoca miglire
                        self.model.set_weights(self.best_weights)

                        new_lr = old_lr * self.factor
                        new_lr = max(new_lr, self.min_lr)

                        logging.info(
                            f"Updating LR (new value = {new_lr}), best score={self.best}"
                        )

                        backend.set_value(self.model.optimizer.lr, new_lr)
                        if self.verbose > 0:
                            print(
                                "\nEpoch %05d: ReduceLROnPlateau reducing learning "
                                "rate to %s." % (epoch + 1, new_lr)
                            )
                        self.cooldown_counter = self.cooldown
                        self.wait = 0
