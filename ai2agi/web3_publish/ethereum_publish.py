import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from datetime import datetime
import os

class EthereumPublisher:
    def __init__(self, infura_url, private_key, contract_address):
        """
        Initialize the EthereumPublisher class with necessary parameters.

        :param infura_url: The Infura URL for connecting to the Ethereum network.
        :param private_key: The private key to sign transactions.
        :param contract_address: The address of the smart contract to interact with.
        """
        # Connect to Ethereum network (Mainnet or Testnet)
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        if self.web3.isConnected():
            print("Connected to Ethereum network.")
        else:
            raise Exception("Failed to connect to Ethereum network.")
        
        # Add POA (Proof of Authority) middleware for testnets like Rinkeby
        self.web3.middleware_stack.inject(geth_poa_middleware, layer=0)

        # Set the private key and public address
        self.private_key = private_key
        self.account = self.web3.eth.account.privateKeyToAccount(private_key)
        self.address = self.account.address

        # Contract details
        self.contract_address = contract_address
        self.contract_abi = self.load_contract_abi()  # ABI for interacting with the contract
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def load_contract_abi(self):
        """
        Load the ABI of the Ethereum contract from a JSON file or another source.
        """
        # Example of loading the ABI from a local file, modify path accordingly
        try:
            with open('contract_abi.json', 'r') as abi_file:
                abi = json.load(abi_file)
            return abi
        except Exception as e:
            print(f"Error loading contract ABI: {e}")
            return None

    def publish_event(self, event_data):
        """
        Publish event data to the Ethereum network by interacting with a smart contract.

        :param event_data: A dictionary containing the data to be published.
        """
        try:
            # Prepare the data to send to the smart contract
            event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = {
                "event_time": event_time,
                "event_data": json.dumps(event_data)  # Convert event data to JSON string
            }

            # Create transaction data
            transaction = self.contract.functions.publishEvent(
                data['event_time'], data['event_data']
            ).buildTransaction({
                'from': self.address,
                'gas': 2000000,
                'gasPrice': self.web3.toWei('20', 'gwei'),
                'nonce': self.web3.eth.getTransactionCount(self.address),
            })

            # Sign the transaction
            signed_txn = self.web3.eth.account.signTransaction(transaction, self.private_key)

            # Send the transaction
            txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print(f"Transaction hash: {txn_hash.hex()}")

            # Wait for the transaction to be mined
            txn_receipt = self.web3.eth.waitForTransactionReceipt(txn_hash)
            print(f"Transaction receipt: {txn_receipt}")
            
            # Successfully published event
            print("Event successfully published to Ethereum.")

        except Exception as e:
            print(f"Error publishing event: {e}")

# Example of running the EthereumPublisher
if __name__ == "__main__":
    INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
    PRIVATE_KEY = 'YOUR_PRIVATE_KEY'
    CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS'

    publisher = EthereumPublisher(INFURA_URL, PRIVATE_KEY, CONTRACT_ADDRESS)

    # Example event data (from MotherCell or any other part of the system)
    event_data = {
        "cell_id": "MOTHER_CELL_1",
        "task": "Analyze environment",
        "status": "Completed",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Publish event to Ethereum network
    publisher.publish_event(event_data)
