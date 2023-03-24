import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import Config

class BlobStorageClient():
    def __init__(self, account_name, account_key):
        self.account_name = account_name
        self.account_key = account_key
        self.account_url = f'https://{self.account_name}.blob.core.windows.net'

        self.blob_service_client = BlobServiceClient(account_url= self.account_url, credential= self.account_key)
    
    def download_blob(self, container_name, blob_name):
        config = Config()

        download_path = os.path.join(config.get_option("APP_CONFIG", "DOWNLOAD_DIRECTORY"), blob_name)

        container_client = self.blob_service_client.get_container_client(container= container_name)
        print("\nDownloading blob to \n\t" + download_path)

        with open(download_path, "wb") as download_file:
            download_file.write(container_client.download_blob(blob_name).readall())
            