import os
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio
from omegaconf import DictConfig
from tqdm import tqdm

from car_azimuth_predictor.utils.training_tools import np_shift_05_pi


def generate_features(config: DictConfig):
    """Function to generate the features"""
    features = ["azimuth", "elevation", "distance"]
    df_list = []
    root_path = Path(os.getcwd())

    dataset_base_path = root_path / config.data_processing.dataset_base_path

    # Read train and validation lists
    with open(os.path.join(dataset_base_path, "Image_sets", "car_imagenet_train.txt")) as f:
        train_set = set(f.read().splitlines())
    with open(os.path.join(dataset_base_path, "Image_sets", "car_imagenet_val.txt")) as f:
        val_set = set(f.read().splitlines())

    # Read annotations
    for annotation_file in tqdm(
        sorted(
            os.listdir(os.path.join(dataset_base_path, "Annotations", "car_imagenet"))
        )
    ):
        # Reading annotations from matlab file
        mat = sio.loadmat(
            os.path.join(
                os.path.join(dataset_base_path, "Annotations", "car_imagenet"),
                annotation_file,
            )
        )

        filebase = annotation_file.split(".")[0]
        is_train = filebase in train_set
        if not is_train:
            assert filebase in val_set, f"File {filebase} is not in train or val set"

        row = [annotation_file.split(".")[0], is_train]
        for el in features:
            feature = mat["record"][0, 0]["objects"][0, 0]["viewpoint"][0, 0][el][0, 0]
            row.append(feature)

        df_list.append(row)

    df = pd.DataFrame(df_list, columns=["image_path", "is_train"] + features)

    # Convert azimuth and file_path
    df["image_path"] = df["image_path"].apply(
        lambda x: os.path.join(dataset_base_path, "Images", "car_imagenet", x) + ".JPEG"
    )
    df["is_train"] = df["is_train"].astype("int")

    df["azimuth_radians"] = df["azimuth"] / 180 * np.pi
    df["azimuth_radians_shifted"] = df["azimuth_radians"].apply(
        lambda x: x if x < np.pi else x - 2 * np.pi
    )
    df["azimuth_radians_abs"] = np.abs(df["azimuth_radians_shifted"])
    df["azimuth_norm_abs"] = df["azimuth_radians_abs"] / np.pi

    df["azimuth_radians_shifted_0.5_pi"] = np_shift_05_pi(df["azimuth_radians"])
    df["azimuth_radians_shifted_0.5_pi_norm_abs"] = np.abs(
        df["azimuth_radians_shifted_0.5_pi"] / np.pi
    )

    df["azimuth_radians_sign"] = np.sign(df["azimuth_radians_shifted"])
    df["azimuth_sin"] = np.sin(df["azimuth_radians"])
    df["azimuth_cos"] = np.cos(df["azimuth_radians"])

    df.to_csv(
        os.path.join(dataset_base_path, config.data_processing.csv_filename),
        index=False,
    )
