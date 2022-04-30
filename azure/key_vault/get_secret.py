# Secrets can be read back from Key Vault as long as the code's
# identity context is authorized to access the vault.
#
# Reference: https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python

import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

from dotenv import load_dotenv

load_dotenv()

key_vault_name = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{key_vault_name}.vault.azure.net"

default_credential = DefaultAzureCredential(exclude_visual_studio_code_credential=True)

client = SecretClient(vault_url=KVUri, credential=default_credential)

secret_name = 'example'

secret_value = client.get_secret(secret_name).value

print('Secret with name {} has a value of {} in key vault {}'.format(secret_name, secret_value, key_vault_name))