import hydra
from hydra import compose, initialize

current_config = {}


def load_config():
    global current_config

    # Initilize Hydra
    hydra.core.global_hydra.GlobalHydra.instance().clear()
    initialize(config_path="../config", version_base="1.2")

    # Get the configurations
    config = compose(config_name="main.yaml", overrides=[])
    current_config = config

    return config
