import os
import os.path
import configparser
from blobretriever.config import Config
from blobretriever.initialize import initialize
from blobretriever.blobstorageclient import BlobStorageClient

if __name__ == '__main__':
    initialize()
    config = Config()
    print(config.get_option('APP_CONFIG', 'DOWNLOAD_DIRECTORY'))

    blob_storage_client = BlobStorageClient(config.get_option('BLOB_CONFIG', 'ACCOUNT_NAME'), config.get_option('BLOB_CONFIG', 'ACCOUNT_KEY'))
