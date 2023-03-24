import typer
from config import Config
from blobstorageclient import BlobStorageClient
from directory import check

app = typer.Typer(no_args_is_help=True)

@app.callback()
def main() -> None:
    return

@app.command()
def list_blobs(
    container_name: str = typer.Argument(...)
) -> None:
    blob_storage_client = __get_blob_storage_client()
    blob_list = blob_storage_client.list_blobs_from_container(container_name)
    for blob_name in blob_list:
        typer.secho(blob_name)

@app.command()
def download_blobs(
    container_name: str = typer.Argument(...),
    download_path: str = typer.Option(
        None,
        '-p',
        '--path'
    )

) -> None:
    if (download_path != None):
        if (check(download_path) == False):
            print(f'{download_path} is not a valid download path')
            return

    blob_storage_client = __get_blob_storage_client()
    blob_storage_client.download_blobs_from_container(container_name, download_path)

@app.command()
def set_download_path(
    download_path: str = typer.Argument(...)
) -> None:
    config = Config()

    if (check(download_path) == False):
            print(f'{download_path} is not a valid file path')
            return
    
    config.set_directory(download_path)


def __get_blob_storage_client():
    config = Config()
    return BlobStorageClient(config.get_option('BLOB_CONFIG', 'ACCOUNT_NAME'), config.get_option('BLOB_CONFIG', 'ACCOUNT_KEY'))
    