
# environmental_impact.py
# Module 3: Simple Environmental Impact Estimator

class EnvironmentalImpactEstimator:
    def __init__(self, battery_batch):
        self.battery = battery_batch

    def estimate_landfill_diversion_kg(self):
        """Estimates physical weight saved from a landfill (~45 grams per 1,000 mAh)."""
        estimated_weight_kg = (self.battery.initial_capacity_mah / 1000.0) * 0.045
        return round(estimated_weight_kg, 3)

    def calculate_environmental_report(self):
        tier = self.battery.assess_lifecycle_tier()
        weight_diverted = self.estimate_landfill_diversion_kg()

        report = {
            "batch_id": self.battery.batch_id,
            "diverted_mass_kg": weight_diverted,
            "triage_category": tier
        }

        if "Tier 3" in tier:
            report["action_impact"] = "Critical Material Recovery: Prevented heavy metal leaching into soil/water tables."
        elif "Tier 2" in tier:
            report["action_impact"] = "Second-Life Extension: Offset carbon footprint by avoiding new manufacturing."
        else:
            report["action_impact"] = "Primary Use Active: Retaining utility in current device."

        return report
