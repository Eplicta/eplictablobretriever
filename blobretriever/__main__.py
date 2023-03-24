import os
import os.path
import configparser
from config import Config
from initialize import initialize
from blobstorageclient import BlobStorageClient
import cli

__app_name__ = "blobretriever"

def main():
    initialize()
    cli.app(prog_name= __app_name__)

if __name__ == '__main__':
    main()
