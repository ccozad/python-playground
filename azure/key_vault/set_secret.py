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
secret_value = 'foobar'

client.set_secret(secret_name, secret_value)

print('Secret with name {} written to key vault {}'.format(secret_name, key_vault_name))