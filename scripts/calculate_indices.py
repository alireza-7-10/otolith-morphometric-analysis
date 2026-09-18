import pandas as pd

# Load processed otolith data
data = pd.read_csv("../data/processed/otolith_descriptive_indices.csv")

# Display the dataset
print("Otolith Morphometric Dataset")
print(data)

# Basic summary by species
summary = data.groupby("Species")[
    ["E_WO_OL", "R_RostrumLength_OL", "S_SulcusArea_TotalArea"]
].agg(["mean", "std", "min", "max"])

print("\nDescriptive Summary by Species:")
print(summary)
