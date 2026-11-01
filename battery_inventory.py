# battery_inventory.py
# Module 1: Battery Inventory & E-Waste Classification
# Part of battery-ewaste-lifecycle-tracker

class BatteryInventoryManager:
    def __init__(self):
        self.inventory_records = []

    def log_batch(self, batch_id, chemistry, initial_capacity_mah, current_capacity_mah, source_device):
        """Logs a new batch of batteries entering the e-waste collection center."""
        record = {
            "batch_id": batch_id,
            "chemistry": chemistry.upper(),
            "initial_capacity_mah": initial_capacity_mah,
            "current_capacity_mah": current_capacity_mah,
            "source_device": source_device
        }
        self.inventory_records.append(record)
        print(f"[LOGGED] Batch {batch_id} ({chemistry}) from {source_device} added to inventory.")

    def get_inventory_summary(self):
        """Returns the full list of logged battery inventory."""
        return self.inventory_records

# --- Testing Module 1 ---
if __name__ == "__main__":
    manager = BatteryInventoryManager()
    manager.log_batch("LIB-101", "NMC", 3000, 2500, "Smartphone")
    manager.log_batch("LIB-102", "LFP", 5000, 3400, "Solar Backup")
    manager.log_batch("LIB-103", "NMC", 2500, 1100, "Laptop")
    
    print(f"\nTotal Batches Logged: {len(manager.get_inventory_summary())}")
