import os
from dotenv import load_dotenv
from web3 import Web3, exceptions

load_dotenv()

RPC_URL = os.getenv("SEPOLIA_RPC_URL")
if not RPC_URL:
    raise SystemExit("SEPOLIA_RPC_URL çevre değişkeni bulunamadı. .env dosyanı kontrol et.")

try:
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.is_connected():
        raise ConnectionError("Sepolia ağına bağlanamadım.")
except (exceptions.InvalidURL, ConnectionError) as err:
    raise SystemExit(f"Bağlantı hatası: {err}")

chain_id = web3.eth.chain_id
latest_block = web3.eth.block_number
print(f"Sepolia bağlantısı tamam! Chain ID: {chain_id}, son blok: {latest_block}")
