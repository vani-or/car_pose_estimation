import pickle as pkl

import optuna
import tensorflow as tf
from tensorflow.python.keras.utils.layer_utils import count_params

from car_azimuth_predictor.config import load_config
from car_azimuth_predictor.dataset_generation import generate_datasets
from car_azimuth_predictor.utils.training_tools import (
    horizontal_flip_pose_sin_cos_output,
    tf_acc_pi_6_sin_cos_output,
    tf_mean_absolute_angle_error_sin_cos_output,
    tf_median_absolute_angle_error_sin_cos_output,
    tf_r2_angle_score_sin_cos_output,
    tf_rmse_angle_sin_cos_output,
)

# import sys
# sys.path.insert(0, str(Path().resolve().parent))
try:
    load_config()
    from car_azimuth_predictor.config import current_config
    from car_azimuth_predictor.model_generation import generate_model
except ImportError:
    raise

gt_cols = ["azimuth_sin", "azimuth_cos"]


loss = tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")

input_layer = tf.keras.layers.Input(shape=(1280,))


def objective(trial):
    n_neurons_middle_layer = trial.suggest_int(
        "n_neurons_middle_layer", low=0, high=256, step=32
    )
    dropout_rate = trial.suggest_float("dropout_rate", low=0.1, high=0.5, step=0.01)
    learning_rate = trial.suggest_loguniform("learning_rate", low=0.00002, high=0.002)
    batch_size = trial.suggest_categorical("batch_size", [32, 64, 128])
    should_augment = trial.suggest_int(
        "should_augment", low=0, high=1
    )  # emulate boolean

    train_dataset, validation_dataset, test_dataset = generate_datasets(
        current_config,
        gt_cols=gt_cols,
        pose_flip_fn=horizontal_flip_pose_sin_cos_output,
        batch_size=batch_size,
        augment=should_augment,
    )

    in_to_dense = tf.keras.layers.Dropout(dropout_rate, name="Dropout")(input_layer)

    if n_neurons_middle_layer:
        activation_fn_middle_layer = trial.suggest_categorical(
            "activation_fn_middle_layer", ["relu", "leaky_relu", "linear", "tanh"]
        )
        in_to_dense = tf.keras.layers.Dense(
            n_neurons_middle_layer,
            activation=activation_fn_middle_layer,
            name="mlp_middle",
        )(in_to_dense)

    mlp_output = tf.keras.layers.Dense(2, activation="tanh", name="mlp_output")(
        in_to_dense
    )
    bottom = tf.keras.models.Model(inputs=input_layer, outputs=mlp_output)

    model = generate_model(current_config, bottom=bottom)

    print("Number of trainable weights:", count_params(model.trainable_weights))
    # model.summary()

    optimizer = tf.keras.optimizers.Adamax(learning_rate=learning_rate)
    from car_azimuth_predictor.train_model import train_model

    metrics = [
        tf_mean_absolute_angle_error_sin_cos_output,
        tf_rmse_angle_sin_cos_output,
        tf_r2_angle_score_sin_cos_output,
        tf_median_absolute_angle_error_sin_cos_output,
        tf_acc_pi_6_sin_cos_output,
    ]
    train_history, current_datetime_strgfied = train_model(
        current_config,
        model=model,
        train_dataset=train_dataset,
        validation_dataset=validation_dataset,
        optimizer=optimizer,
        loss=loss,
        metrics=metrics,
        verbose=2,
    )

    metrics = model.evaluate(validation_dataset, verbose=2)

    return metrics[0]  # val_loss


study = optuna.create_study()
study.optimize(objective, n_trials=25)


with open("hyperparameter_search/approach1_study.pkl", "wb") as fp:
    pkl.dump(study, fp)
