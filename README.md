
# Battery E-Waste Lifecycle Tracker

A Python-based engineering toolkit and educational repository designed to model, track, and triage lithium-ion and mixed battery chemistries for e-waste management and circular economy applications.

## 🌍 The Global Context & Motivation

Modern electronic waste is growing five times faster than documented e-waste recycling globally. According to the **Global E-waste Monitor** (jointly published by the International Telecommunication Union [ITU] and the United Nations Institute for Training and Research [UNITAR]), the world generated a record **62 million tonnes of e-waste** in a single year. 

While large appliances and heavy equipment dominate the physical weight of total e-waste, lithium-ion batteries and small IT devices carry a disproportionately high environmental and chemical hazard due to heavy metal leaching (cobalt, nickel, and lithium). 

### Project Purpose
The **Battery E-Waste Lifecycle Tracker** bridges the gap between macro-level statistics and local triage. Rather than trying to map global tonnage on a local scale, this tool provides modular Python scripts to inventory, assess State of Health (SoH), route second-life candidates, and calculate precise landfill mass diversion for individual battery batches.

---
### 📚 Data References
* **Global E-waste Generation:** *Global E-waste Monitor 2024* – International Telecommunication Union (ITU) and United Nations Institute for Training and Research (UNITAR).

## 🌍 The Mission
With the rapid growth of portable electronics and electric vehicles, lithium-ion battery waste presents a major environmental challenge to landfills. This project applies clean Object-Oriented Programming (OOP) principles in Python to automate the health assessment, degradation tracking, and end-of-life recycling triage of battery cells.

---

## 🛠️ Key Technical Features

1. **State of Health (SoH) & Capacity Fade Tracking:** 
   - Calculates percentage capacity loss relative to initial manufactured capacity.
   - Normalizes health metrics across different cell sizes and chemistries.

2. **Three-Tier Circular Economy Triage:**
   - **Tier 1 (Primary Use):** State of Health $\ge 80\%$. Fit for continued primary use.
   - **Tier 2 (Second-Life Candidate):** State of Health between $50\%$ and $79.9\%$. Suitable for low-drain or stationary energy storage (e.g., solar LED setups, backup routers).
   - **Tier 3 (Immediate Recycle / Mineral Recovery):** State of Health $< 50\%$ or severe degradation requiring hydrometallurgical processing to recover critical materials (Lithium, Cobalt, Nickel).

3. **Object-Oriented Programming (OOP) Architecture:**
   - **Encapsulation:** Protects internal telemetry (like current capacity and voltage) using name-mangling (`__`) and controlled getter/setter methods.
   - **Inheritance:** Uses a base class (`BaseBattery`) to eliminate code duplication across specialized battery chemistries (`LithiumIonBattery`, `LeadAcidBattery`).
   - **Polymorphism:** Implements unified interface methods (like `.get_recycling_protocol()`) so different battery types handle their own disposal rules automatically.

---

## 📁 Repository Structure

```text
battery-ewaste-lifecycle-tracker/
│
├── battery_classes.py          # OOP architectural pillars (SecureBattery, BaseBattery, etc.)
├── battery_metrics.py          # Capacity fade & State of Health calculations
├── battery_inventory.py        # Module 1: Inventory logging & batch tracking
├── environmental_impact.py     # Module 3: Landfill mass diversion & toxic recovery
├── environmental_plot.py       # Python script generating the impact comparison chart
├── triage_playground.ipynb     # Interactive Jupyter/Colab testing notebook
├── ewaste_impact_comparison.png# Generated visualization asset
└── README.md                   # Project documentation with macro stats & citations

```

## 🚀 Getting Started
Ensure you have Python 3 installed on your system.

Clone or download this repository locally.

Run the core metrics script to see the triage system in action:

Bash
```
python battery_metrics.py
```
## 💡 Learning & Development
This repository serves as both a practical environmental engineering utility and a personal learning workshop exploring Python data structures, algorithms, and clean software architecture. Contributions, forks, and expansions are welcome!

