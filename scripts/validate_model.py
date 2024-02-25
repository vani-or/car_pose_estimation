import argparse
from pprint import pprint
from keras.models import load_model

from car_azimuth_predictor.config import load_config
from car_azimuth_predictor.dataset_generation import generate_datasets
from car_azimuth_predictor.utils.training_tools import (
    horizontal_flip_pose_sin_cos_output,
    # Approach 2
    horizontal_flip_pose_double_sigmoid,
)


def main(approach, model_path: str, current_config=None):
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

    model = load_model(model_path)

    metrics = model.evaluate(validation_dataset, verbose=2)

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--approach", type=str, help="Approach to use (1 = Sin/Cos, 2 = Directional discriminators)", choices=["1", "2"])
    parser.add_argument("--model_path", type=str, help="Path to the model to validate")

    args = parser.parse_args()

    current_config = load_config()

    metrics = main(approach=args.approach, model_path=args.model_path, current_config=current_config)
    pprint(metrics)
