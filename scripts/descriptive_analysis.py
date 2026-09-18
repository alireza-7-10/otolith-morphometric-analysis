import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set up dynamic paths (relative to project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
# New path to the CSV file located inside the processed folder:
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'otolith_descriptive_indices.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

print("Reading data...")
df = pd.read_csv(DATA_PATH)
print("Data loaded successfully.")

# 1. Calculate descriptive statistics
metrics = ['E_WO_OL', 'R_RostrumLength_OL', 'S_SulcusArea_TotalArea']
summary_stats = df.groupby('Species')[metrics].agg(['mean', 'std', 'min', 'max'])
summary_stats.to_csv(os.path.join(RESULTS_DIR, 'descriptive_statistics_summary.csv'))
print("Summary table saved to results/descriptive_statistics_summary.csv")

# 2. Plot boxplots
print("\nPlotting charts...")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

titles = ['E Index (WO/OL)', 'R Index (Rostrum/OL)', 'S Index (Sulcus/Total)']

for ax, metric, title in zip(axes, metrics, titles):
    sns.boxplot(x='Species', y=metric, data=df, ax=ax, hue='Species', palette='Set2', legend=False)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()

# 3. Save image
save_path = os.path.join(FIGURES_DIR, 'descriptive_boxplots.png')
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.close() 

print("Image saved successfully to figures/descriptive_boxplots.png")
