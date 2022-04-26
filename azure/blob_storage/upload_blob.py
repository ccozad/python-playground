# Default Azure credential will check common credential sources including
# Environment variables, managed identities, visual studio code identity and
# Azure CLI identities.
#
# For more details about Default Azure Credential and the order credentials are
# evaluated see:
# https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
# 
#
# Reference for Container Client
# https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python

import os

from dotenv import load_dotenv

load_dotenv()

from azure.identity import DefaultAzureCredential
from azure.storage.blob import (
    BlobServiceClient
)

if __name__ == "__main__":
    default_credential = DefaultAzureCredential(exclude_visual_studio_code_credential=True)
    account_url = os.getenv('STORAGE_ACCOUNT')
    container_name = os.getenv('CONTAINER_NAME')
    blob_name = os.getenv('BLOB_NAME')

    blob_service_client = BlobServiceClient(
        credential=default_credential, 
        account_url=account_url)

    container_client = blob_service_client.get_container_client(container_name)
    if container_client.exists():
        print('Container {} exists in account {}'.format(container_name, account_url))
        blob_client = container_client.get_blob_client(blob_name)
        if blob_client.exists():
            print('Blob {} already exists!'.format(blob_name))
        else:
            data = 'Hello world!'
            blob_client.upload_blob(data)
            print('Blob {} uploaded'.format(blob_name))
    else:
        print('Container {} does not exist, unable to upload blob!'.format(container_name))
