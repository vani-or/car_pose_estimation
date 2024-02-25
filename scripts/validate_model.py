import argparse
from pprint import pprint
from keras.models import load_model

from car_azimuth_predictor.config import load_config
from car_azimuth_predictor.dataset_generation import generate_datasets
from car_azimuth_predictor.visualize import visualize_single_predictions
import tensorflow_hub as hub
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


def main(approach, model_path: str, current_config=None, visualizations_path: str = None):
    assert approach in ["1", "2"], "Approach must be 1 or 2"

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
        batch_size=32,
        augment=False,
    )

    model = load_model(model_path, custom_objects={
        "KerasLayer": hub.KerasLayer,
        "angle_double_output_loss": angle_double_output_loss,
        "tf_mean_absolute_angle_error_double_sigmoid": tf_mean_absolute_angle_error_double_sigmoid,
        "tf_rmse_angle_score_double_sigmoid": tf_rmse_angle_score_double_sigmoid,
        "tf_r2_angle_score_double_sigmoid": tf_r2_angle_score_double_sigmoid,
        "tf_median_absolute_angle_error_double_sigmoid": tf_median_absolute_angle_error_double_sigmoid,
        "tf_acc_pi_6_double_sigmoid": tf_acc_pi_6_double_sigmoid,
        "horizontal_flip_pose_double_sigmoid": horizontal_flip_pose_double_sigmoid,
        "tf_mean_absolute_angle_error_sin_cos_output": tf_mean_absolute_angle_error_sin_cos_output,
        "tf_rmse_angle_sin_cos_output": tf_rmse_angle_sin_cos_output,
        "tf_r2_angle_score_sin_cos_output": tf_r2_angle_score_sin_cos_output,
        "tf_median_absolute_angle_error_sin_cos_output": tf_median_absolute_angle_error_sin_cos_output,
        "tf_acc_pi_6_sin_cos_output": tf_acc_pi_6_sin_cos_output,
        "horizontal_flip_pose_sin_cos_output": horizontal_flip_pose_sin_cos_output,
    })

    metric_values = model.evaluate(validation_dataset, verbose=1)
    metric_names = [
        'loss',
        'mean_absolute_angle_error',
        'median_absolute_angle_error',
        'r2',
        'rmse',
        'acc_pi_6',
    ]

    if visualizations_path is not None:
        visualize_single_predictions(model, validation_dataset, save_path=visualizations_path)

    return dict(zip(metric_names, metric_values))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--approach", type=str, help="Approach to use (1 = Sin/Cos, 2 = Directional discriminators)", choices=["1", "2"])
    parser.add_argument("--model_path", type=str, help="Path to the model to validate")
    parser.add_argument("--visualizations_path", type=str, default=None, help="Path to save visualizations")

    args = parser.parse_args()

    current_config = load_config()

    metrics = main(
        approach=args.approach,
        model_path=args.model_path,
        current_config=current_config,
        visualizations_path=args.visualizations_path
    )
    pprint(metrics)
