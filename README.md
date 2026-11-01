


# Battery E-Waste Lifecycle Tracker

A Python-based engineering toolkit and educational repository designed to model, track, and triage lithium-ion and mixed battery chemistries for e-waste management and circular economy applications.

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
├── battery_metrics.py          # Core classes, SoH calculations, and triage logic
├── oop_tutorial_battery_ewaste.md # Comprehensive OOP tutorial (Encapsulation, Inheritance, Polymorphism)
└── README.md                   # Project documentation
```
##🚀 Getting Started
Ensure you have Python 3 installed on your system.

Clone or download this repository locally.

Run the core metrics script to see the triage system in action:

```
Bash

python battery_metrics.py

```
##💡 Learning & Development
This repository serves as both a practical environmental engineering utility and a personal learning workshop exploring Python data structures, algorithms, and clean software architecture. Contributions, forks, and expansions are welcome!
