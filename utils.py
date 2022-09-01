import os.path
import shutil

import yaml
from yaml import SafeLoader


def read_yaml_file(yaml_file):
    # Open the file and load the file
    with open(yaml_file) as f:
        # return data as dictionary
        data = yaml.load(f, Loader=SafeLoader)
    return data


def check_path(path, silent=False):
    if os.path.isdir(path):
        if not silent:
            print(f"{path} exists...")
    else:
        os.mkdir(path)
        if not silent:
            print(f"{path} created...")


def remove_path(path, silent=False):
    if os.path.isdir(path):
        shutil.rmtree(path)
        if not silent:
            print(f"{path} removed...")
