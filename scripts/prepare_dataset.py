import argparse
from car_azimuth_predictor.data_gathering import collect_data
from car_azimuth_predictor.feature_generation import generate_features
from car_azimuth_predictor.split_dataset import split_dataset
from car_azimuth_predictor.config import load_config


def main():
    parser = argparse.ArgumentParser(description="Prepare the dataset")
    parser.add_argument(
        "--dataset_location",
        type=str,
        default="data/PASCAL3D+_release1.1.zip",
        help="Path to the PASACL3D+ dataset zip file (version 1.1)",
    )
    args = parser.parse_args()

    current_config = load_config()

    # collect_data(current_config)
    # split_dataset(current_config)
    generate_features(current_config)


if __name__ == "__main__":
    main()
