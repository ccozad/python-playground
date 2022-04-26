# Default Azure credential will check common credential sources including
# Environment variables, managed identities, visual studio code identity and
# Azure CLI identities.
#
# For more details about Default Azure Credential and the order credentials are
# evaluated see:
# https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
# 
#
# Reference for list_containers for Blob Service Client
# https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python#azure-storage-blob-blobserviceclient-list-containers

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

    blob_service_client = BlobServiceClient(
        credential=default_credential, 
        account_url=account_url)

    containers = blob_service_client.list_containers()

    print('Containers found in account {}'.format(account_url))
    for container in containers:
        print( ' - {}'.format(container.name))