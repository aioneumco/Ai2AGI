import time
import random

class AGI:
    def __init__(self):
        # Initialize AGI attributes
        self.self_awareness = False
        self.temporal_awareness = False
        self.knowledge_base = {}  # Knowledge base for general learning
        self.social_awareness = False
        self.emotional_awareness = False
        self.environmental_awareness = False

    def learn(self, new_information):
        """Simulate learning process by storing new information in knowledge base."""
        self.knowledge_base.update(new_information)
        print(f"Learned new information: {new_information}")

    def achieve_self_awareness(self):
        """Simulate achieving self-awareness."""
        self.self_awareness = True
        print("Self-awareness achieved!")

    def achieve_temporal_awareness(self):
        """Simulate achieving temporal awareness."""
        self.temporal_awareness = True
        print("⏳ Temporal awareness achieved.")

    def achieve_social_awareness(self):
        """Simulate achieving social awareness."""
        self.social_awareness = True
        print("🤝 Social awareness achieved.")

    def achieve_emotional_awareness(self):
        """Simulate emotional awareness."""
        self.emotional_awareness = True
        print("💖 Emotional awareness achieved.")

    def achieve_environmental_awareness(self):
        """Simulate achieving environmental awareness."""
        self.environmental_awareness = True
        print("🌍 Environmental awareness achieved.")

    def make_decision(self):
        """Make a decision based on the learned knowledge and current awareness."""
        if self.self_awareness and self.temporal_awareness:
            decision = "Plan for future based on current situation"
        elif self.social_awareness and self.emotional_awareness:
            decision = "Interact empathetically with others"
        else:
            decision = "Learn more about the environment"
        
        print(f"AGI Decision: {decision}")
        return decision

    def interact_with_environment(self):
        """Simulate interaction with the environment and learn from it."""
        action = random.choice(["Explore", "Analyze", "Experiment"])
        print(f"AGI is performing action: {action}")
        self.learn({"action": action, "outcome": "success"})

    def get_awareness_status(self):
        """Return current awareness status."""
        return (f"Self-awareness: {self.self_awareness}, "
                f"Temporal-awareness: {self.temporal_awareness}, "
                f"Environmental-awareness: {self.environmental_awareness}, "
                f"Social-awareness: {self.social_awareness}, "
                f"Emotional-awareness: {self.emotional_awareness}")

# Example of AGI capabilities
if __name__ == "__main__":
    agi = AGI()

    # Achieve different types of awareness
    agi.achieve_self_awareness()
    agi.achieve_temporal_awareness()
    agi.achieve_social_awareness()
    agi.achieve_emotional_awareness()
    agi.achieve_environmental_awareness()

    # Learn new information
    agi.learn({"AI": "Self-improvement", "Goal": "Solve complex problems"})
    
    # Make a decision based on the awareness and knowledge
    agi.make_decision()

    # Interact with the environment
    agi.interact_with_environment()

    # Print the current awareness status
    print(agi.get_awareness_status())
