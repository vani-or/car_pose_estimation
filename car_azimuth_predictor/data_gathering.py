import os
import shutil
import tempfile
from pathlib import Path

from omegaconf import DictConfig

from car_azimuth_predictor.utils.zip_tools import unzip


def collect_data(config: DictConfig):
    """Function to collect data into the raw folder"""

    output_path = Path(os.getcwd()) / config.data_gathering.local_dataset_path
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path, exist_ok=True)

    unzip(
        file_path=config.data_gathering.pascal_zip_file_location,
        target_path=output_path,
        members=config.data_gathering.members_to_extract,
    )

    print(f"Save the output to {output_path}")
