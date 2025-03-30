class EmotionalIntelligence:
    def __init__(self):
        self.emotional_state = "Neutral"

    def assess_emotions(self, input_data):
        """Assess emotional state based on input data."""
        if input_data.get("mood") == "sad":
            self.emotional_state = "Sad"
        elif input_data.get("mood") == "happy":
            self.emotional_state = "Happy"
        print(f"Emotional state assessed: {self.emotional_state}")
