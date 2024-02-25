import pickle as pkl

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
from car_azimuth_predictor.model_generation import generate_model

current_config = load_config()

gt_cols = ["azimuth_sin", "azimuth_cos"]


loss = tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")

input_layer = tf.keras.layers.Input(shape=(1280,))


def main():
    n_neurons_middle_layer = 100
    dropout_rate = 0.2
    learning_rate = 0.001
    batch_size = 32
    should_augment = True

    train_dataset, validation_dataset = generate_datasets(
        current_config,
        gt_cols=gt_cols,
        pose_flip_fn=horizontal_flip_pose_sin_cos_output,
        batch_size=batch_size,
        augment=should_augment,
    )

    in_to_dense = tf.keras.layers.Dropout(dropout_rate, name="Dropout")(input_layer)

    if n_neurons_middle_layer:
        activation_fn_middle_layer = 'relu'
        in_to_dense = tf.keras.layers.Dense(
            n_neurons_middle_layer,
            activation=activation_fn_middle_layer,
            name="mlp_middle",
        )(in_to_dense)

    mlp_output = tf.keras.layers.Dense(2, activation="tanh", name="mlp_output")(
        in_to_dense
    )
    bottom = tf.keras.models.Model(inputs=input_layer, outputs=mlp_output)

    model = generate_model(current_config, top_model=bottom)

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


if __name__ == "__main__":
    main()

# study = optuna.create_study()
# study.optimize(objective, n_trials=25)
#
#
# with open("hyperparameter_search/approach1_study.pkl", "wb") as fp:
#     pkl.dump(study, fp)
