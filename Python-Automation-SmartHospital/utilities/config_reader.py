import os
from configparser import ConfigParser

def get_value(filename, category, key):
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "configurations", filename)
    config.read(config_path)
    return config.get(category, key)
