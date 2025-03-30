class StemCellRegeneration:
    def __init__(self):
        self.regeneration_state = "Idle"

    def regenerate(self):
        """Trigger the regeneration of stem cells."""
        self.regeneration_state = "Regenerating"
        print("Stem cells are regenerating.")

    def stop_regeneration(self):
        """Stop the regeneration process."""
        self.regeneration_state = "Idle"
        print("Stem cell regeneration stopped.")
