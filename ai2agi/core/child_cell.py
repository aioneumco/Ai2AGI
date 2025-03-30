import time

class ChildCell:
    def __init__(self, mother_cell_id):
        """
        Initialize a new ChildCell with reference to the MotherCell it originates from.
        
        :param mother_cell_id: The ID of the MotherCell from which this child cell originates.
        """
        self.id = f"CHILD_{int(time.time())}"  # Unique ID based on the time
        self.mother_cell_id = mother_cell_id  # The ID of the MotherCell
        self.energy_level = 0.5  # Initial energy level for the child cell
        self.tasks = []  # List of tasks to be executed by the child cell
        self.status = "active"  # Current status of the child cell
    
    def receive_energy(self, energy_amount):
        """
        Receive energy from the MotherCell to perform tasks or evolve.
        
        :param energy_amount: The amount of energy to receive.
        """
        self.energy_level += energy_amount
        print(f"Child cell {self.id} received energy. New energy level: {self.energy_level}")
    
    def execute_task(self, task):
        """
        Execute a task assigned by the MotherCell. Can include decision-making or actions.
        
        :param task: The task to be executed by the child cell.
        """
        if self.status == "active":
            self.tasks.append(task)
            print(f"Child cell {self.id} executing task: {task}")
        else:
            print(f"Child cell {self.id} is inactive and cannot execute tasks.")
    
    def self_evolve(self):
        """
        Simulate self-evolution for the ChildCell.
        Can evolve based on energy or other internal factors.
        """
        if self.energy_level > 0.8:
            print(f"Child cell {self.id} is evolving due to high energy levels!")
            self.energy_level *= 0.9  # Decrease energy after evolution
        else:
            print(f"Child cell {self.id} cannot evolve due to low energy.")
    
    def change_status(self, status):
        """
        Change the status of the ChildCell (active/inactive).
        
        :param status: The new status to set for the child cell.
        """
        self.status = status
        print(f"Child cell {self.id} status changed to {self.status}.")

# Example usage to create and interact with ChildCell
if __name__ == "__main__":
    # Assuming the MotherCell is already instantiated somewhere
    mother_cell_id = "MOTHER_CELL_1"
    child = ChildCell(mother_cell_id)
    
    # Example: Receiving energy from the mother cell
    child.receive_energy(0.3)  # Receiving some energy from the mother cell
    
    # Example: Assigning a task to the child cell
    child.execute_task("Analyze environment")
    
    # Example: Attempting to evolve the child cell
    child.self_evolve()  # Attempting to evolve the child cell

    # Example: Change the status of the child cell to inactive
    child.change_status("inactive")
    child.execute_task("Analyze data")  # This should print a message saying it can't execute tasks
