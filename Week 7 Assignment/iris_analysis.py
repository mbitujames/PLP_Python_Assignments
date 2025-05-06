# iris_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check data types and missing values
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species and calculating mean
print("\nAverage Measurements per Species:")
print(df.groupby("species").mean())

# Task 3: Visualizations
sns.set(style="whitegrid")

# 1. Line Chart - Plotting sepal length trend across samples
plt.figure(figsize=(10, 5))
plt.plot(df['sepal length (cm)'], label='Sepal Length (cm)', color='blue')
plt.title("Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='muted')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram - Distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, color='orange', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# Observations
print("\nFindings:")
print("- Sepal and petal lengths vary significantly across species.")
print("- Setosa generally has shorter petals and wider sepals.")
print("- Strong correlation between petal length and species.")
print("- Line plot shows a clear variation pattern for sepal length across samples.")

