import configparser
import os
import sys


def read_Config(path, key):
    if not os.path.exists(path):
        print('CONFIG NOT EXIST')
        sys.exit()

    config = configparser.ConfigParser()
    config.read(path)

    value = config.get("Settings", key)
    return value
