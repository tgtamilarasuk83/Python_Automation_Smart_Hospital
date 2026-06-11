from configparser import ConfigParser

config = ConfigParser()
def get_value(filename,category, key):
    config.read("./configurations/"+filename)
    return config.get(category, key)