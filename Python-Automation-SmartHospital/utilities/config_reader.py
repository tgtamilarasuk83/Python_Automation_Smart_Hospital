from configparser import ConfigParser


def get_value(filename,category, key):
    config = ConfigParser()
    config.read("./configurations/"+filename)
    return config.get(category, key)