# Scripts

This folder contains Python scripts for analyzing otolith morphometric data.

## descriptive_analysis.py
This script performs the following tasks:
1. Reads processed data from `data/processed/otolith_descriptive_indices.csv`
2. Calculates descriptive statistics (mean, standard deviation, min, max) for E, R, and S indices
3. Saves the summary table in the `results/` folder
4. Plots comparative boxplots between the three species and saves them in the `figures/` folder

**How to run:**
From the project root folder, run the following command:
```bash
python scripts/descriptive_analysis.py
**Dependencies**
Make sure the required libraries are installed:Dependencies
Make sure the required libraries are installed:
pip install pandas matplotlib seaborn
