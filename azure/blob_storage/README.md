# Environment Variables

Change `example.env` to `.env`

 - `STORAGE_ACCOUNT` Url for blob storage account, usually of the form `https://<storage account name>.blob.core.windows.net/`
 - `CONTAINER_NAME` Name of container to interact with, for example `usercontent`
 - `BLOB_NAME` Name of the blob to interact with, for example `test.txt`

# Install Dependencies

1. Change into the /azure/blob_storage directory
2. Create a virtual environment
3. `pip install -r requirements.txt`

# Execution Order

All of the examples have guards if they are run before preconditions are met. The recomended order to run things and have something actually happen is

 1. `create_container.py`
 2. `list_containers.py`
 3. `upload_blob.py`
 4. `list_blobs.py`
 5. `download_blob.py`