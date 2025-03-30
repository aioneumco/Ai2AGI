import json
import time

class ComplianceMonitor:
    def __init__(self, mother_cell):
        """
        Initialize the ComplianceMonitor with a reference to the MotherCell.
        
        :param mother_cell: The MotherCell instance.
        """
        self.mother_cell = mother_cell  # Reference to the MotherCell instance
        self.compliance_data = {}  # Data structure to track compliance information
    
    def track_task_compliance(self, child_cell_id, task, status, error_message=None):
        """
        Track the compliance of tasks being executed by child cells.
        
        :param child_cell_id: The ID of the child cell.
        :param task: The task being tracked.
        :param status: The status of the task (e.g., 'completed', 'pending').
        :param error_message: Optional error message if the task fails.
        """
        timestamp = time.time()
        compliance_status = {
            "task": task,
            "status": status,
            "timestamp": timestamp,
            "error_message": error_message
        }
        
        if child_cell_id not in self.compliance_data:
            self.compliance_data[child_cell_id] = []
        
        self.compliance_data[child_cell_id].append(compliance_status)
        
        # Print compliance status for the child cell
        print(f"Compliance for Child Cell {child_cell_id}: Task '{task}' - {status}")
        if error_message:
            print(f"Error: {error_message}")
    
    def check_compliance(self):
        """
        Check the overall compliance of the system.
        This function can be extended to check different compliance conditions.
        """
        print("Checking compliance across all child cells...")

        for child_cell_id, tasks in self.compliance_data.items():
            for task_info in tasks:
                if task_info["status"] != "completed":
                    print(f"Compliance Warning: Child Cell {child_cell_id} failed to complete task: {task_info['task']}")
                    if task_info["error_message"]:
                        print(f"Error Message: {task_info['error_message']}")
        
        # Example: Return if all tasks were completed successfully
        all_compliant = all(task["status"] == "completed" for tasks in self.compliance_data.values() for task in tasks)
        
        if all_compliant:
            print("All child cells are compliant with the required tasks.")
        else:
            print("Some child cells are not compliant with required tasks.")
    
    def save_compliance_report(self, file_path):
        """
        Save the compliance report to a JSON file.
        
        :param file_path: The file path where the report will be saved.
        """
        with open(file_path, "w") as f:
            json.dump(self.compliance_data, f, indent=4)
        
        print(f"Compliance report saved to {file_path}")

# Example usage to demonstrate the ComplianceMonitor functionality
if __name__ == "__main__":
    # Assuming MotherCell is already created, passing it to ComplianceMonitor
    mother_cell = {
        "id": "MOTHER_CELL_1",
        "children": ["CHILD_1", "CHILD_2"]  # Example children cells
    }

    monitor = ComplianceMonitor(mother_cell)
    
    # Example of tracking tasks for child cells
    monitor.track_task_compliance("CHILD_1", "Analyze environment", "completed")
    monitor.track_task_compliance("CHILD_2", "Perform self-evolution", "pending", error_message="Insufficient energy")
    
    # Check overall compliance status
    monitor.check_compliance()
    
    # Save the compliance report
    monitor.save_compliance_report("C:\\pr\\Free_Knowledge_Perfection\\reports\\compliance_report.json")
