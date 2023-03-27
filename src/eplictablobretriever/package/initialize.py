import os.path
from config import Config

def initialize():
    config = Config()
    config.attempt_set_directory('C:/test/blobretriever')
