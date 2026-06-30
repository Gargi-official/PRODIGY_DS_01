import pandas as pd
import matplotlib.pyplot as plt

# Load the population data
population = pd.read_csv("population.csv", skiprows=4)

# Load country metadata
metadata = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_478913.csv")

# Keep only actual countries (Region is not empty)
metadata = metadata[metadata["Region"].notna()]

# Merge metadata with population data
df = population.merge(
    metadata[["Country Code", "Region"]],
    on="Country Code",
    how="inner"
)

# Select year
year = "2023"

# Keep only required columns
df = df[["Country Name", year]]

# Remove missing values
df = df.dropna()

# Convert population to numeric
df[year] = pd.to_numeric(df[year])

# Top 10 populated countries
top10 = df.sort_values(by=year, ascending=False).head(10)

# Plot
plt.figure(figsize=(12,6))

plt.bar(
    top10["Country Name"],
    top10[year],
    color="steelblue",
    edgecolor="black"
)

plt.title("Top 10 Most Populated Countries (2023)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("population_distribution.png", dpi=300)

plt.show()