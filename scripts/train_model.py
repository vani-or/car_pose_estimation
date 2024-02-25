import argparse
import tensorflow as tf
from tensorflow.python.keras.utils.layer_utils import count_params

from car_azimuth_predictor.train_model import train_model
from car_azimuth_predictor.config import load_config
from car_azimuth_predictor.dataset_generation import generate_datasets
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
)
from car_azimuth_predictor.model_generation import generate_model


def main(approach: str, save_model_path: str, train_history_path: str,  current_config=None):
    assert approach in ["1", "2"], "Approach must be 1 or 2"

    n_neurons_middle_layer = 100
    dropout_rate = 0.2
    learning_rate = 0.001
    batch_size = 32
    should_augment = True

    if approach == "1":
        pose_flip_fn = horizontal_flip_pose_sin_cos_output
        gt_cols = ["azimuth_sin", "azimuth_cos"]
    else:
        pose_flip_fn = horizontal_flip_pose_double_sigmoid
        gt_cols = ['azimuth_norm_abs', 'azimuth_radians_shifted_0.5_pi_norm_abs']

    train_dataset, validation_dataset = generate_datasets(
        current_config,
        gt_cols=gt_cols,
        pose_flip_fn=pose_flip_fn,
        batch_size=batch_size,
        augment=should_augment,
    )

    input_layer = tf.keras.layers.Input(shape=(1280,))
    in_to_dense = tf.keras.layers.Dropout(dropout_rate, name="Dropout")(input_layer)

    if n_neurons_middle_layer:
        activation_fn_middle_layer = 'relu'
        in_to_dense = tf.keras.layers.Dense(
            n_neurons_middle_layer,
            activation=activation_fn_middle_layer,
            name="mlp_middle",
        )(in_to_dense)

    if approach == "1":
        mlp_output = tf.keras.layers.Dense(2, activation="tanh", name="mlp_output")(in_to_dense)
        bottom = tf.keras.models.Model(inputs=input_layer, outputs=mlp_output)

        # Metrics definition
        metrics = [
            tf_mean_absolute_angle_error_sin_cos_output,
            tf_rmse_angle_sin_cos_output,
            tf_r2_angle_score_sin_cos_output,
            tf_median_absolute_angle_error_sin_cos_output,
            tf_acc_pi_6_sin_cos_output,
        ]

        # Loss
        loss = tf.keras.losses.MeanSquaredError(reduction="auto", name="mean_squared_error")
    else:
        angle1_sigmoid_output = tf.keras.layers.Dense(1, activation="sigmoid", name="angle1_output")(in_to_dense)
        angle2_sigmoid_output = tf.keras.layers.Dense(1, activation="sigmoid", name="angle2_output")(in_to_dense)

        angle_concatenated = tf.keras.layers.Concatenate(axis=1, name="concatenate_angles_2_vars")([angle1_sigmoid_output, angle2_sigmoid_output])

        bottom = tf.keras.models.Model(inputs=input_layer, outputs=angle_concatenated)

        # Metrics definition
        metrics = [
            tf_mean_absolute_angle_error_double_sigmoid,
            tf_median_absolute_angle_error_double_sigmoid,
            tf_r2_angle_score_double_sigmoid,
            tf_rmse_angle_score_double_sigmoid,
            tf_acc_pi_6_double_sigmoid,
        ]

        # Loss
        loss = angle_double_output_loss

    model = generate_model(current_config, top_model=bottom)

    print("Number of trainable weights:", count_params(model.trainable_weights))
    # model.summary()

    optimizer = tf.keras.optimizers.Adamax(learning_rate=learning_rate)

    train_history = train_model(
        current_config,
        model=model,
        train_dataset=train_dataset,
        validation_dataset=validation_dataset,
        optimizer=optimizer,
        loss=loss,
        metrics=metrics,
        verbose=2,
        save_model_path=save_model_path,
        train_history_path=train_history_path
    )

    metrics = model.evaluate(validation_dataset, verbose=1)

    return metrics[0]  # val_loss


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--approach", type=str, help="Approach to use (1 = Sin/Cos, 2 = Directional discriminators)", choices=["1", "2"])
    parser.add_argument("--n_neurons_middle_layer", type=int, default=100)
    parser.add_argument("--dropout_rate", type=float, default=0.2)
    parser.add_argument("--learning_rate", type=float, default=0.001)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--should_augment", type=bool, default=True)
    parser.add_argument("--save_model_path", type=str, help="Path to save the model")
    parser.add_argument("--train_history_path", type=str, help="Path to save the training history")

    args = parser.parse_args()

    current_config = load_config()

    main(
        approach=args.approach,
        save_model_path=args.save_model_path,
        train_history_path=args.train_history_path,
        current_config=current_config
    )
