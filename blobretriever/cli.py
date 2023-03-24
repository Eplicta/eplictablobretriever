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
    config = Config()

    blob_storage_client = BlobStorageClient(config.get_option('BLOB_CONFIG', 'ACCOUNT_NAME'), config.get_option('BLOB_CONFIG', 'ACCOUNT_KEY'))
    blob_list = blob_storage_client.list_blobs_from_container(container_name)
    for blob_name in blob_list:
        typer.secho(blob_name)

@app.command()
def download_blobs(
    container_name: str = typer.Argument(...),
    file_path: str = typer.Option(
        None,
        '-p',
        '--path'
    )

) -> None:
    config = Config()

    if (file_path != None):
        if (check(file_path) == False):
            print(f'{file_path} is not a valid file path')
            return

    blob_storage_client = BlobStorageClient(config.get_option('BLOB_CONFIG', 'ACCOUNT_NAME'), config.get_option('BLOB_CONFIG', 'ACCOUNT_KEY'))
    blob_storage_client.download_blobs_from_container(container_name, file_path)
    