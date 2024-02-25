from typing import List
from zipfile import ZipFile


def unzip(file_path: str, target_path: str, members: List[str]):
    # https://stackoverflow.com/a/1760715
    # it seems like the python standard library zipfile performs well
    # https://stackoverflow.com/a/72903814/5733813
    with ZipFile(file_path) as z:
        for file in z.namelist():
            if any([x for x in members if file.startswith(x)]):
                z.extract(file, target_path)
