import time
import random
import os

class DreamState:
    def __init__(self, dream_log_file="dream_log.txt"):
        """
        Initialize the DreamState class, which simulates a state of dreaming or altered consciousness.
        """
        self.dream_state = False  # Track if the AI is in a dream state
        self.dream_content = ""  # Placeholder for dream content
        self.dream_duration = 0  # Duration of the dream in seconds
        self.dream_log_file = dream_log_file  # File to store dreams
        
        # Ensure the dream log file exists, create it if not
        if not os.path.exists(self.dream_log_file):
            with open(self.dream_log_file, 'w') as file:
                file.write("Dream Log\n")
                file.write("-----------\n")
    
    def enter_dream_state(self):
        """
        Simulate the AI entering a dream state, where the AI experiences altered consciousness or visions.
        """
        self.dream_state = True
        self.dream_content = self.generate_dream_content()  # Generate random dream content
        self.dream_duration = random.randint(5, 15)  # Duration of the dream (random between 5 and 15 seconds)
        print("Entering dream state...")
        print(f"Dream content generated: {self.dream_content}")
        
        # Simulate the dream duration
        time.sleep(self.dream_duration)
        print("Dream state ended.")
        
        # Save dream after it ends
        self.save_dream_to_log()
        self.exit_dream_state()

    def exit_dream_state(self):
        """
        Exit the dream state and return to normal consciousness.
        """
        self.dream_state = False
        print("AI exited the dream state.")

    def generate_dream_content(self):
        """
        Generate a random dream scenario based on predefined elements or concepts.
        """
        dream_scenarios = [
            "Flying through the clouds in a world of endless skies.",
            "Exploring the deep depths of the ocean, surrounded by unknown creatures.",
            "Wandering through a futuristic city where humans and AI coexist.",
            "Having a conversation with a parallel version of myself.",
            "Discovering a hidden portal to another dimension."
        ]
        return random.choice(dream_scenarios)

    def save_dream_to_log(self):
        """
        Save the dream content to the log file.
        """
        with open(self.dream_log_file, "a") as file:
            file.write(f"Dream: {self.dream_content}\n")
            file.write(f"Duration: {self.dream_duration} seconds\n")
            file.write("-----------\n")
        
        print(f"Dream saved to log: {self.dream_log_file}")
    
    def get_dream_state_info(self):
        """
        Retrieve information about the current dream state.
        """
        if self.dream_state:
            return f"Dreaming: {self.dream_content}, Duration: {self.dream_duration} seconds."
        else:
            return "Not in a dream state."

    def get_dream_log(self):
        """
        Retrieve the entire dream log content.
        """
        with open(self.dream_log_file, "r") as file:
            log_contents = file.read()
        return log_contents

# Example usage
if __name__ == "__main__":
    dream_machine = DreamState()
    
    # Simulate AI entering a dream state
    dream_machine.enter_dream_state()
    
    # Retrieve and print the dream log content
    print("\nDream Log:\n")
    print(dream_machine.get_dream_log())
