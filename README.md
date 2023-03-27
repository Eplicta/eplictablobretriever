# Eplicta Blob Retriever
This is a Python command-line application designed to retrieve data from Azure Blob Storage.

## Installation

Python version 3.11 or higher is required for this application

### Clone repository
Clone the repository to your local machine

To run anything using a cloned repository you need to setup a python virtual environment in the cloned repository. https://docs.python.org/3/library/venv.html

Install the required dependencies by running ´pip install -r requirements.txt´ in your terminal or command prompt. Remember that this as well as running the actual application's command needs to be done in the virtual environment.

### Install as package
run ´pip install -i https://test.pypi.org/simple/ eplictablobretriever´.

If installation fails, additional dependencies may need to be installed.

## Usage
1. Open a terminal or command prompt in the directory where the application is installed
2. To view available commands, run ´python -m eplictablobretriever´
3. Configure blob storage credentials by running ´python -m eplictablobretriever set-blob-config [ACCOUNT_NAME] [ACCOUNT_KEY]´. Replace [ACCOUNT_NAME] and [ACCOUNT_KEY] with the appropriate details
4. Once the blob config has been set, the application is ready to go

## Commands
The following commands are available for use with this tool:
- ´list-blobs´: List all blobs in the specified container
- ´download-blobs´: Download all blobs in the specified container
- ´set-blob-config´: Set Blob Config
- ´set-download-path´: Set the path to where the files will be downloaded to

Examples
- To download all blobs in the "mycontainer" container: ´python -m eplictablobcontainer download-blobs mycontainer´

## Limitations
This tool currently only supports downloading from Azure Blob Storage. Uploading is not supported.
This tool currently only supports authentication with account key and account name.
