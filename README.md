# 🔋 Battery E-Waste Lifecycle Tracker & Circular Economy Toolkit

> *"Tracking battery inventory, triage pathways, and environmental lifecycles from acquisition to responsible e-waste recycling."*

A Python-based engineering toolkit and educational repository designed to model, track, and triage lithium-ion and mixed battery chemistries for e-waste management and circular economy applications.

---

## 📌 Project Architecture & Modular Design

To make this codebase clean, maintainable, and structured for educational tutorials, the logic is separated into dedicated classes and modules rather than a single monolithic script:

```text
battery-ewaste-lifecycle-tracker/
│
├── README.md                          # Master project documentation
├── requirements.txt                   # Python dependencies (Pandas, Matplotlib, NumPy)
│
├── modules/                           # Core modular classes
│   ├── __init__.py
│   ├── inventory_logger.py            # Class 1: BatteryInventoryLogger
│   ├── ewaste_triage.py               # Class 2: EWasteTriageAnalyzer
│   └── impact_visualizer.py           # Class 3: EnvironmentalImpactPlotter
│
├── notebooks/                         # Step-by-step tutorial notebooks
│   └── 01_battery_lifecycle_tutorial.ipynb
│
└── data/                              # Sample logs and triage datasets
    └── sample_battery_inventory.csv
```

---

## 🛠️ Core Classes & Tutorial Breakdown

### 1. `BatteryInventoryLogger` (`inventory_logger.py`)
* **Purpose:** Handles ingestion, validation, and structured logging of battery chemistry types (Li-ion, NiMH, Lead-Acid), capacity ratings, and operational cycle counts.
* **Key Functionality:** Tracks acquisition dates, health status, and current storage states.

### 2. `EWasteTriageAnalyzer` (`ewaste_triage.py`)
* **Purpose:** Evaluates end-of-life status based on voltage degradation, physical swelling flags, or capacity drop below threshold limits.
* **Key Functionality:** Automatically classifies cells into triage paths: **Reuse**, **Repurpose (Second Life)**, or **Recycle / Safe Disposal**.

### 3. `EnvironmentalImpactPlotter` (`impact_visualizer.py`)
* **Purpose:** Generates automated Matplotlib / Seaborn environmental impact plots.
* **Key Functionality:** Visualises toxic material diversion (Cobalt, Nickel, Lead) kept out of municipal landfills through proper recycling triage.

---

## 🚀 How to Run the Code

**1. Clone the repository:**
```bash
git clone https://github.com/ananyaja/battery-ewaste-lifecycle-tracker.git
cd battery-ewaste-lifecycle-tracker
```

**2. Set up the environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Launch the tutorial notebook:**
```bash
jupyter notebook notebooks/01_battery_lifecycle_tutorial.ipynb
```

---

## 📊 Analytical Findings & Circular Economy Insights
* **Triage Efficiency:** Automated categorisation drastically reduces the time required to sort mixed inventory batches into safe recycling streams.
* **Resource Recovery:** Tracking cumulative capacity loss highlights optimal windows for repurposing energy storage cells into low-drain backup systems before full material recycling becomes necessary.

---

📬 **Authors & Collaboration:** 
* **Lead Researcher & Domain Expert:** Ananyaja Debadipta
* **AI Collaborator & Technical Co-Pilot:** Gemini (Google AI)

*Developed collaboratively as an open-source technical partnership bridging independent data research and structured software design.*
