from core.mother_cell import MotherCell
from core.child_cell import ChildCell

if __name__ == "__main__":
    # Initialize MotherCell and its children
    mother_cell = MotherCell()
    mother_cell.create_child()

    # Example: Distribute tasks and evolve
    child_cells = [ChildCell(parent_id=mother_cell.id)]
    mother_cell.tasks = ["Task 1", "Task 2", "Task 3"]
    mother_cell.distribute_tasks(child_cells)
    mother_cell.evolve()
