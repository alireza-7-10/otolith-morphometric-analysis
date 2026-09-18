import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os

# تنظیم مسیرها به صورت داینامیک (نسبت به روت پروژه)
# این کد فرض می‌کند شما از پوشه اصلی (main) دستور python scripts/descriptive_analysis.py را اجرا می‌کنید.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
DATA_PATH = os.path.join(BASE_DIR, 'data', 'otolith_descriptive_indices.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

print("در حال خواندن داده‌ها...")
df = pd.read_csv(DATA_PATH)
print("داده‌ها با موفقیت خوانده شدند.")

# ۱. محاسبه آماره‌های توصیفی
metrics = ['E_WO_OL', 'R_RostrumLength_OL', 'S_SulcusArea_TotalArea']
summary_stats = df.groupby('Species')[metrics].agg(['mean', 'std', 'min', 'max'])
summary_stats.to_csv(os.path.join(RESULTS_DIR, 'descriptive_statistics_summary.csv'))
print("جدول خلاصه در results/descriptive_statistics_summary.csv ذخیره شد.")

# ۲. رسم نمودارهای جعبه‌ای
print("\nدر حال رسم نمودارها...")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

titles = ['E Index (WO/OL)', 'R Index (Rostrum/OL)', 'S Index (Sulcus/Total)']

for ax, metric, title in zip(axes, metrics, titles):
    sns.boxplot(x='Species', y=metric, data=df, ax=ax, hue='Species', palette='Set2', legend=False)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()

# ۳. ذخیره تصویر
save_path = os.path.join(FIGURES_DIR, 'descriptive_boxplots.png')
plt.savefig(save_path, dpi=300, bbox_inches='tight')
plt.close() 

print("تصویر با موفقیت در figures/descriptive_boxplots.png ذخیره شد.")
