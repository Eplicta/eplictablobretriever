import os
import os.path
import configparser
from config import Config

def initialize():
    config = Config()
    config.attempt_set_directory('C:/test/blobretriever')
