import os
import os.path
import configparser
from config import Config
from initialize import initialize

if __name__ == '__main__':
    initialize()
    config = Config()
    print(config.get_option('APP_CONFIG', 'DIRECTORY'))
    