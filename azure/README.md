# Introduction

All of the interactions with Azure services require an Azure account.

# Authentication

The examples all take advantage of the Default Azure Credential class. The Default Azure credential will check common credential sources including environment variables, managed identities, visual studio code identity and Azure CLI identities.

For more details about Default Azure Credential and the order credentials are evaluated see: https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python

# Environment Variables

Each group of examples will typically require one or more environment variables that will be specific to your Azure subscription. Typically you will need to change `example.env` to `.env` and populate the correct values.

# Services

 - [Blob Storage](/azure/blob_storage/) ubiqutous file storage on Azure
   - [Create container](/azure/blob_storage/create_container.py) 
     - `python3 create_container.py`
   - [List containers](/azure/blob_storage/list_containers.py) 
     - `python3 list_containers.py`
   - [Upload blob](/azure/blob_storage/upload_blob.py) 
     - `python3 upload_blob.py`
   - [List blobs](/azure/blob_storage/list_blobs.py) 
     - `python3 list_blobs.py`
   - [Download blob](/azure/blob_storage/download_blob.py) 
     - `python3 download_blob.py`

**[Back to start](https://github.com/ccozad/python-playground)**