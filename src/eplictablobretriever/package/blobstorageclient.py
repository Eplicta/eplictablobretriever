import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import Config

class BlobStorageClient():
    def __init__(self, account_name, account_key):
        self.config = Config()

        self.account_name = account_name
        self.account_key = account_key
        self.account_url = f'https://{self.account_name}.blob.core.windows.net'

        self.blob_service_client = BlobServiceClient(account_url= self.account_url, credential= self.account_key)
    
    def download_blob(self, container_name, blob_name, file_path= None):
        download_path = os.path.join(self.config.get_option("APP_CONFIG", "DOWNLOAD_DIRECTORY"), blob_name)
        if (file_path != None):
                download_path = os.path.join(file_path, blob_name)
                
        container_client = self.blob_service_client.get_container_client(container= container_name)

        self.__download_blob(self, container_client, download_path, blob_name)

    def download_blobs_from_container(self, container_name, file_path= None):
        container_client, exists = self.__get_container_client(container_name)
        if (exists == False):
            return

        blob_list = container_client.list_blob_names()

        for blob_name in blob_list:
            download_path = os.path.join(self.config.get_option("APP_CONFIG", "DOWNLOAD_DIRECTORY"), blob_name)
            if (file_path != None):
                download_path = os.path.join(file_path, blob_name)

            self.__download_blob(container_client, download_path, blob_name)

    def list_blobs_from_container(self, container_name):
        container_client, exists = self.__get_container_client(container_name)
        if (exists == False):
            return
        
        blob_list = container_client.list_blob_names()

        return blob_list

    def __download_blob(self, container_client, download_path, blob_name):
        print("\nDownloading blob to \n\t" + download_path)

        os.makedirs(os.path.dirname(download_path), exist_ok=True)
        with open(download_path, "wb") as download_file:
            download_file.write(container_client.download_blob(blob_name).readall())

    def __get_container_client(self, container_name):
        container_client = self.blob_service_client.get_container_client(container= container_name)

        if (container_client.exists() == False):
            print(f'Container {container_client.container_name} does not exist in storage account {self.account_name}')
            return container_client, False

        return container_client, True
