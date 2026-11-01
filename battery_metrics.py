# --- Battery Metrics Class ---
# battery_metrics.py
# Part of battery-ewaste-lifecycle-tracker
# A Python class to track health fade and categorize lithium-ion batteries for e-waste management.

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
        2. Second-Life Candidate: Health between 50% and 79.9% (e.g., solar lighting, backup power)
        3. Immediate Recycle: Health < 50% (or severe degradation requiring material recovery)
        """
        soh = self.calculate_state_of_health()
        
        if soh >= 80.0:
            return "Tier 1: Fit for Primary Use"
        elif 50.0 <= soh < 80.0:
            return "Tier 2: Second-Life Candidate (Stationary / Low-Drain)"
        else:
            return "Tier 3: Immediate Recycle / Mineral Recovery"

# --- Testing the Class with Multiple Scenarios ---
if __name__ == "__main__":
    # Simulating different batteries entering an e-waste collection center
    battery_1 = BatteryBatch("LIB-101", "NMC", initial_capacity_mah=3000, current_capacity_mah=2500) # ~83.3% Health
    battery_2 = BatteryBatch("LIB-102", "LFP", initial_capacity_mah=5000, current_capacity_mah=3400) # 68% Health
    battery_3 = BatteryBatch("LIB-103", "NMC", initial_capacity_mah=2500, current_capacity_mah=1100) # 44% Health

    batch_list = [battery_1, battery_2, battery_3]

    print("--- E-Waste & Lifecycle Triage Report ---\n")
    for bat in batch_list:
        print(f"Batch ID: {bat.batch_id} | Chemistry: {bat.cell_type}")
        print(f"  - State of Health (SoH): {bat.calculate_state_of_health()}%")
        print(f"  - Triage Status: {bat.assess_lifecycle_tier()}")
        print("-" * 45)
