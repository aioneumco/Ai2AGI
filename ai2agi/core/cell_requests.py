import json
import requests

class CellRequestHandler:
    def __init__(self, api_url):
        """
        Initializes the request handler for interacting with external APIs or services.
        
        :param api_url: The base URL of the API or endpoint that handles cell operations.
        """
        self.api_url = api_url  # The base URL for the API that interacts with the cells (e.g., "http://example.com/api")
        self.headers = {'Content-Type': 'application/json'}  # The headers for the requests

    def create_cell(self, cell_data):
        """
        Sends a request to create a new cell (daughter or child cell) based on given data.
        
        :param cell_data: Dictionary containing the necessary data to create the cell.
        :return: The response from the creation request, typically the created cell's information.
        """
        try:
            # POST request to create a new cell
            response = requests.post(f"{self.api_url}/create_cell", headers=self.headers, data=json.dumps(cell_data))
            response.raise_for_status()  # Check for HTTP errors
            print(f"Cell created successfully with ID: {response.json()['id']}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating cell: {e}")
            return None

    def update_cell(self, cell_id, updated_data):
        """
        Sends a PUT request to update an existing cell's properties.
        
        :param cell_id: The unique identifier of the cell to update.
        :param updated_data: Dictionary containing updated information for the cell.
        :return: The updated cell's data.
        """
        try:
            # PUT request to update the cell's information
            response = requests.put(f"{self.api_url}/cells/{cell_id}/update", headers=self.headers, data=json.dumps(updated_data))
            response.raise_for_status()  # Check for HTTP errors
            print(f"Cell with ID {cell_id} updated successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating cell {cell_id}: {e}")
            return None

    def delete_cell(self, cell_id):
        """
        Sends a DELETE request to remove a specific cell based on its ID.
        
        :param cell_id: The unique identifier of the cell to delete.
        :return: Boolean value indicating success or failure.
        """
        try:
            # DELETE request to remove a cell
            response = requests.delete(f"{self.api_url}/cells/{cell_id}/delete", headers=self.headers)
            response.raise_for_status()  # Check for HTTP errors
            print(f"Cell with ID {cell_id} deleted successfully.")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error deleting cell {cell_id}: {e}")
            return False

    def get_cell_status(self, cell_id):
        """
        Retrieve the current status of a cell using a GET request.
        
        :param cell_id: The unique identifier of the cell to retrieve.
        :return: Dictionary containing the cell's current status and data.
        """
        try:
            # GET request to fetch the status of the specified cell
            response = requests.get(f"{self.api_url}/cells/{cell_id}", headers=self.headers)
            response.raise_for_status()  # Check for HTTP errors
            print(f"Cell {cell_id} status retrieved successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving cell {cell_id} status: {e}")
            return None


# Example usage in context of the 'MotherCell' and its child cells:

if __name__ == "__main__":
    api_url = "http://example.com/api"  # Replace with your actual API URL
    cell_handler = CellRequestHandler(api_url)
    
    # Example data for creating a new child cell:
    new_child_data = {
        "type": "daughter",
        "parent_cell_id": "MOTHER_CELL_1",
        "status": "active",
        "tasks": ["task1", "task2"],
        "chromosomes": {"chromosome_1": "data", "chromosome_2": "data"}
    }

    # Create new child cell
    created_cell = cell_handler.create_cell(new_child_data)
    
    if created_cell:
        cell_id = created_cell["id"]  # Assuming the ID is part of the response
        
        # Update the cell (e.g., change its status or add tasks)
        updated_data = {"status": "inactive", "tasks": ["task1", "task3"]}
        updated_cell = cell_handler.update_cell(cell_id, updated_data)

        # Retrieve the status of the cell
        cell_status = cell_handler.get_cell_status(cell_id)
        if cell_status:
            print(f"Current cell status: {cell_status}")

        # Delete the child cell after operation (optional, for cleanup)
        success = cell_handler.delete_cell(cell_id)
        if success:
            print("Cell deleted successfully.")
