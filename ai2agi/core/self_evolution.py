import random
import time

class SelfEvolution:
    def __init__(self):
        # Initialize SelfEvolution with relevant attributes
        self.evolution_occurred = False
        self.last_evolution_time = None

    def trigger_evolution(self):
        """Simulate the self-evolution process with a chance."""
        if random.random() > 0.7:  # 30% chance for evolution
            self.evolution_occurred = True
            self.last_evolution_time = time.time()
            print("Evolution occurred!")
        else:
            self.evolution_occurred = False
            print(" No evolution this time.")

    def get_evolution_status(self):
        """Return the evolution status of the cell."""
        if self.evolution_occurred:
            return f"Last evolution at {time.ctime(self.last_evolution_time)}"
        else:
            return "No evolution occurred yet."

# Example of using self-evolution process
if __name__ == "__main__":
    evolution = SelfEvolution()
    evolution.trigger_evolution()
    print(evolution.get_evolution_status())
