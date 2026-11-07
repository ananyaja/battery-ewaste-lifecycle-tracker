# battery_inventory.py
# Module 1: Battery Inventory & E-Waste Classification

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
