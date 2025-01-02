# Environment Variables

Change `example.env` to `.env`

 - `KEY_VAULT_NAME` Unique key vault name

# Install Dependencies

1. Change into the /azure/key_vault directory
2. Create a virtual environment
3. `pip install -r requirements.txt`

# Execution Order

All of the examples have guards if they are run before preconditions are met. The recommended order to run things and have something actually happen is

 1. `set_secret.py`
 2. `get_secret.py`

**[Back to start](https://github.com/ccozad/python-playground)**