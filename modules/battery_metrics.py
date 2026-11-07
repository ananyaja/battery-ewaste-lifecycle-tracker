# battery_metrics.py
# Module 2: Capacity Fade & Cycle Life Calculation

class BatteryBatch:
    def __init__(self, batch_id, cell_type, initial_capacity_mah, current_capacity_mah):
        self.batch_id = batch_id
        self.cell_type = cell_type
        self.initial_capacity_mah = initial_capacity_mah
        self.current_capacity_mah = current_capacity_mah

    def calculate_capacity_fade(self):
        """Calculates the percentage of capacity lost (fade)."""
        fade_percentage = ((self.initial_capacity_mah - self.current_capacity_mah) / self.initial_capacity_mah) * 100
        return round(fade_percentage, 2)

    def calculate_state_of_health(self):
        """Calculates current State of Health (SoH) percentage."""
        return round(100.0 - self.calculate_capacity_fade(), 2)

    def assess_lifecycle_tier(self):
        """
        Categorizes the battery into three circular economy tiers:
        1. Primary Use: Health >= 80%
        2. Second-Life Candidate: Health between 50% and 79.9%
        3. Immediate Recycle: Health < 50%
        """
        soh = self.calculate_state_of_health()
        if soh >= 80.0:
            return "Tier 1: Fit for Primary Use"
        elif 50.0 <= soh < 80.0:
            return "Tier 2: Second-Life Candidate (Stationary / Low-Drain)"
        else:
            return "Tier 3: Immediate Recycle / Mineral Recovery"
