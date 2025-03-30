class TaskDistribution:
    def __init__(self):
        self.task_queue = []

    def assign_task_to_cell(self, cell, task):
        """Assign a task to a specific cell."""
        cell.assign_task(task)
        print(f"Task '{task}' assigned to {cell.id}.")

    def distribute_tasks(self, cells, tasks):
        """Distribute tasks to a list of cells."""
        for i, cell in enumerate(cells):
            task = tasks[i % len(tasks)]  # Distribute tasks cyclically
            self.assign_task_to_cell(cell, task)

# Example of distributing tasks among cells
if __name__ == "__main__":
    task_dist = TaskDistribution()
    cells = [ChildCell(parent_id="MOTHER_CELL_1"), GrandchildCell(parent_id="CHILD_1001")]
    tasks = ["Task 1: Environmental Analysis", "Task 2: Self-Evolution"]
    task_dist.distribute_tasks(cells, tasks)
