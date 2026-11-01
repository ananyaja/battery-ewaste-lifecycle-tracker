# environmental_impact.py
# Module 3: Simple Environmental Impact Estimator
# Part of battery-ewaste-lifecycle-tracker

class EnvironmentalImpactEstimator:
    def __init__(self, battery_batch):
        """
        Takes an instance of BatteryBatch (from battery_metrics.py) 
        to calculate environmental savings.
        """
        self.battery = battery_batch

    def estimate_landfill_diversion_kg(self):
        """
        Estimates the physical weight saved from a landfill 
        (Approximation: ~45 grams per 1,000 mAh of cell capacity).
        """
        estimated_weight_kg = (self.battery.initial_capacity_mah / 1000.0) * 0.045
        return round(estimated_weight_kg, 3)

    def calculate_environmental_report(self):
        """Generates an impact report detailing resource recovery and toxicity prevention."""
        tier = self.battery.assess_lifecycle_tier()
        weight_diverted = self.estimate_landfill_diversion_kg()

        report = {
            "batch_id": self.battery.batch_id,
            "diverted_mass_kg": weight_diverted,
            "triage_category": tier
        }

        if "Tier 3" in tier:
            report["action_impact"] = "Critical Material Recovery: Prevented heavy metal leaching (Lithium/Cobalt/Nickel) into soil/water tables."
        elif "Tier 2" in tier:
            report["action_impact"] = "Second-Life Extension: Offset carbon footprint by avoiding the manufacture of new stationary storage units."
        else:
            report["action_impact"] = "Primary Use Active: Retaining utility in current device; zero waste generated."

        return report

# --- Testing Module 3 ---
if __name__ == "__main__":
    # Importing BatteryBatch logic to test impact estimation
    import sys
    import os
    # Assuming battery_metrics is in the same directory
    from battery_metrics import BatteryBatch

    # Test cases representing different tiers
    bat_recycled = BatteryBatch("LIB-103", "NMC", initial_capacity_mah=2500, current_capacity_mah=1100) # Tier 3
    estimator = EnvironmentalImpactEstimator(bat_recycled)
    
    impact = estimator.calculate_environmental_report()
    print("--- Environmental Impact Report ---")
    print(f"Batch ID: {impact['batch_id']}")
    print(f"Landfill Mass Diverted: {impact['diverted_mass_kg']} kg")
    print(f"Triage Status: {impact['triage_category']}")
    print(f"Ecological Impact: {impact['action_impact']}")
