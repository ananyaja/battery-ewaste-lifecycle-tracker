
# environmental_plot.py
# Generates a comparative visualization of e-waste landfill growth vs. tracked diversion impact.

import matplotlib.pyplot as plt
import pandas as pd

def plot_ewaste_comparison():
    # 1. Macro E-Waste Landfill Data (Simulated global/national trend in kilotons)
    years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
    macro_landfill_kt = [53.6, 57.4, 61.3, 65.0, 68.2, 71.5, 74.7] # Rising global e-waste trajectory
    
    # 2. Cumulative Mass Diverted by Your Local Tracker (in kg scaled for visualization)
    # Showing how systematic triage flattens or offsets cumulative waste locally
    tracked_diversion_kg = [0.0, 1.2, 3.5, 7.8, 14.2, 22.5, 35.0]

    # Create figure with dual subplots to compare macro vs micro impact clearly
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Macro E-Waste Landfill Trend ---
    ax1.plot(years, macro_landfill_kt, marker='o', color='#d9534f', linewidth=2.5, label='Global/National E-Waste Landfill')
    ax1.set_title('Macro Trend: Unmanaged E-Waste Growth', fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('Estimated Landfill Volume (Kilotons)', fontsize=10)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper left')

    # --- Plot 2: Local Tracker Diversion Impact ---
    ax2.bar(years, tracked_diversion_kg, color='#5cb85c', alpha=0.85, width=0.6, label='Tracked Landfill Diversion')
    ax2.set_title('Micro Impact: Cumulative Mass Diverted (Your Tracker)', fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlabel('Year', fontsize=10)
    ax2.set_ylabel('Diverted Mass (kg)', fontsize=10)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper left')

    # Overall layout adjustments
    plt.suptitle('Battery E-Waste Lifecycle Tracker: Macro vs. Micro Environmental Impact', fontsize=14, fontweight='bold', y=1.03)
    plt.tight_layout()

    # Save and display
    plt.savefig('ewaste_impact_comparison.png', dpi=300, bbox_inches='tight')
    print("[SUCCESS] Plot generated and saved as 'ewaste_impact_comparison.png'.")
    plt.show()

if __name__ == "__main__":
    plot_ewaste_comparison()
