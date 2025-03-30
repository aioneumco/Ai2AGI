class DamageRepair:
    def __init__(self):
        self.repair_state = "Idle"

    def repair_damage(self):
        """Repair damaged cells."""
        self.repair_state = "Repairing"
        print("Cell damage is being repaired.")

    def stop_repair(self):
        """Stop the repair process."""
        self.repair_state = "Idle"
        print("Cell repair stopped.")
