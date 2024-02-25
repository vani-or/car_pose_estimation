import os
from pathlib import Path

# import hydra
import pandas as pd
from omegaconf import DictConfig
from sklearn.model_selection import train_test_split


def split_dataset(config: DictConfig):
    """Function to split the dataset"""
    root_path = Path(os.getcwd())

    csv_full_path = root_path / config.dataset_split.csv_path

    df = pd.read_csv(csv_full_path)
    train_ids, val_test_ids = train_test_split(
        list(df.index),
        test_size=1 - config.dataset_split.train_size,
        random_state=config.dataset_split.seed,
    )
    val_ids, test_ids = train_test_split(
        val_test_ids,
        test_size=0.5,
        random_state=config.dataset_split.seed,
    )

    df_train = df.loc[train_ids]
    df_val = df.loc[val_ids]
    df_test = df.loc[test_ids]

    df_train.to_csv(root_path / config.dataset_split.output_root_path / "df_train.csv")
    df_val.to_csv(root_path / config.dataset_split.output_root_path / "df_val.csv")
    df_test.to_csv(root_path / config.dataset_split.output_root_path / "df_test.csv")
