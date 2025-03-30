import ipfshttpclient
import os

class IPFSUploader:
    def __init__(self, ipfs_url='http://localhost:5001'):
        """
        Initialize the IPFSUploader class to interact with the IPFS network.

        :param ipfs_url: The URL of the IPFS node to connect to (default is localhost:5001).
        """
        # Connect to the local IPFS node or a remote one (e.g., Infura IPFS)
        try:
            self.client = ipfshttpclient.connect(ipfs_url)
            print(f"Connected to IPFS node at {ipfs_url}")
        except Exception as e:
            print(f"Error connecting to IPFS: {e}")
            raise

    def upload_file(self, file_path):
        """
        Upload a file to IPFS and return its CID (Content Identifier).
        
        :param file_path: The local path to the file to be uploaded.
        :return: CID (Content Identifier) of the uploaded file.
        """
        try:
            # Ensure file exists
            if not os.path.exists(file_path):
                print(f"File {file_path} does not exist.")
                return None

            # Upload the file to IPFS
            file = self.client.add(file_path)
            cid = file['Hash']  # Get the CID of the uploaded file
            print(f"File uploaded successfully! CID: {cid}")
            return cid
        except Exception as e:
            print(f"Error uploading file to IPFS: {e}")
            return None

    def upload_directory(self, dir_path):
        """
        Upload an entire directory to IPFS and return the CID.

        :param dir_path: The local path to the directory to be uploaded.
        :return: CID (Content Identifier) of the uploaded directory.
        """
        try:
            # Ensure directory exists
            if not os.path.isdir(dir_path):
                print(f"Directory {dir_path} does not exist.")
                return None

            # Upload the directory to IPFS
            result = self.client.add(dir_path, recursive=True)
            cid = result[-1]['Hash']  # Get the CID of the uploaded directory
            print(f"Directory uploaded successfully! CID: {cid}")
            return cid
        except Exception as e:
            print(f"Error uploading directory to IPFS: {e}")
            return None

# Example of using the IPFSUploader class
if __name__ == "__main__":
    # Instantiate the IPFS uploader
    ipfs_uploader = IPFSUploader(ipfs_url="http://localhost:5001")  # Or use remote IPFS like Infura

    # Example file to upload
    file_path = "path_to_your_file.txt"  # Replace with the path of the file you want to upload

    # Upload a file and get the CID
    file_cid = ipfs_uploader.upload_file(file_path)

    if file_cid:
        print(f"Uploaded file's CID: {file_cid}")

    # Example directory to upload
    dir_path = "path_to_your_directory"  # Replace with the path of the directory you want to upload

    # Upload a directory and get the CID
    directory_cid = ipfs_uploader.upload_directory(dir_path)

    if directory_cid:
        print(f"Uploaded directory's CID: {directory_cid}")
