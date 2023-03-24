import os
import os.path
import configparser
from blobretriever.config import Config

def initialize():
    config = Config()
    config.attempt_set_option('APP_CONFIG', 'DOWNLOAD_DIRECTORY', 'C:/test/blobretriever')
