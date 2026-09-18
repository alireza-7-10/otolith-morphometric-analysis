import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# تنظیم مسیرها نسبت به محل قرارگیری اسکریپت
# اگر اسکریپت را از روت (main) اجرا می‌کنید، از مسیرهای 'data/...' استفاده کنید
# در اینجا فرض بر این است که از روت اجرا می‌شود
DATA_PATH = 'data/otolith_descriptive_indices.csv'
RESULTS_DIR = 'results'
FIGURES_DIR = 'figures'

# ساخت پوشه‌ها در صورت عدم وجود
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

print("در حال خواندن داده‌ها...")
# ۱. بارگذاری داده‌ها
df = pd.read_csv(DATA_PATH)

# ۲. محاسبه آماره‌های توصیفی
# گروه‌بندی بر اساس گونه و محاسبه میانگین، انحراف معیار، کمینه و بیشینه
metrics = ['E_WO_OL', 'R_RostrumLength_OL', 'S_SulcusArea_TotalArea']
summary_stats = df.groupby('Species')[metrics].agg(['mean', 'std', 'min', 'max'])

print("\n=== جدول آماره‌های توصیفی ===")
print(summary_stats)

# ذخیره جدول در پوشه results
summary_stats.to_csv(os.path.join(RESULTS_DIR, 'descriptive_statistics_summary.csv'))
print(f"\nجدول خلاصه در {RESULTS_DIR}/descriptive_statistics_summary.csv ذخیره شد.")

# ۳. رسم نمودارهای جعبه‌ای (Boxplots)
print("\nدر حال رسم نمودارها...")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

titles = ['شاخص E (عرض/طول)', 'شاخص R (طول روستروم/طول کل)', 'شاخص S (مساحت سولکوس/مساحت کل)']
colors = ['#66b3ff', '#99ff99', '#ffcc99']

for ax, metric, title, color in zip(axes, metrics, titles, colors):
    sns.boxplot(x='Species', y=metric, data=df, ax=ax, palette=color)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel('')
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, 'descriptive_boxplots.png'), dpi=300)
print(f"نمودارها در {FIGURES_DIR}/descriptive_boxplots.png ذخیره شدند.")
