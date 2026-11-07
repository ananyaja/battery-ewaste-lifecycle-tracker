# --- Battery Classes ---
# battery_classes.py
# Part of battery-ewaste-lifecycle-tracker

# Pillar 1: Encapsulation: Protecting Internal Data

class SecureBattery:
    def __init__(self, battery_id, initial_capacity, current_capacity):
        self.battery_id = battery_id
        self.__initial_capacity = initial_capacity  # Private attribute
        self.__current_capacity = current_capacity  # Private attribute

    # Getter method to safely access private data
    def get_current_capacity(self):
        return self.__current_capacity

    # Setter method to update capacity with validation logic
    def update_capacity(self, new_capacity):
        if new_capacity > self.__initial_capacity:
            raise ValueError("Current capacity cannot exceed initial capacity!")
        self.__current_capacity = new_capacity

# --- Usage ---
battery = SecureBattery("LIB-201", 3000, 2400)

# Direct access like 'print(battery.__current_capacity)' will throw an AttributeError.
# Instead, we use our controlled methods:
print(f"Current Capacity: {battery.get_current_capacity()} mAh")


# Pillar 2: Inheritance (The "Parent-Child" Relationship)


# 1. The Parent (Base) Class - Contains universal traits
class BaseBattery:
    def __init__(self, batch_id, chemistry, capacity_mah):
        self.batch_id = batch_id
        self.chemistry = chemistry
        self.capacity_mah = capacity_mah

    def get_basic_info(self):
        return f"Batch ID: {self.batch_id} | Chemistry: {self.chemistry}"

# 2. The Child Class - Inherits everything from BaseBattery using 'super()'
class LithiumIonBattery(BaseBattery):
    def __init__(self, batch_id, capacity_mah, cycle_count):
        # super() looks up at the Parent class and calls its __init__ method
        super().__init__(batch_id, chemistry="Li-ion", capacity_mah=capacity_mah)
        
        # Adding a unique attribute that ONLY lithium-ion batteries care about
        self.cycle_count = cycle_count

    def assess_lithium_wear(self):
        if self.cycle_count > 500:
            return "High degradation: Route to second-life or recycling."
        return "Normal wear."

#Pillar 3: Polymorphism (Many Forms, Same Command)

class LithiumIon:
    def __init__(self, batch_id):
        self.batch_id = batch_id

    # Specialized method for Lithium-ion disposal
    def get_recycling_protocol(self):
        return f"{self.batch_id}: Discharge, shred in inert atmosphere, extract lithium/cobalt."

class LeadAcid:
    def __init__(self, batch_id):
        self.batch_id = batch_id

    # Method has the EXACT SAME NAME, but completely different logic!
    def get_recycling_protocol(self):
        return f"{self.batch_id}: Neutralize corrosive acid electrolyte, smelt lead grids."

# A function that doesn't care WHAT kind of battery it is, as long as it has .get_recycling_protocol()
def process_ewaste_batch(battery_list):
    for bat in battery_list:
        # Polymorphism in action: Python automatically calls the correct protocol for that specific object
        print(bat.get_recycling_protocol())

# --- Usage ---
bin_contents = [
    LithiumIon("LIB-901"),
    LeadAcid("LAB-402")
]

process_ewaste_batch(bin_contents)
