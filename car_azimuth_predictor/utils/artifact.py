from typing import Any

import cloudpickle


def save(obj: Any, filename: str) -> Any:
    with open(filename, "wb") as file:
        return cloudpickle.dump(obj, file)


def load(filename: str) -> Any:
    with open(filename, "rb") as file:
        return cloudpickle.load(file)
