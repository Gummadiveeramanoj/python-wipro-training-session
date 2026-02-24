import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join("config", "config.ini"))

def get_config(key):
    return config["DEFAULT"][key]
