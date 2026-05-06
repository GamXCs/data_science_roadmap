"""

Week 2 Day 5 - Exploratoary Data Analysis
Full EDA pipeline on the Iris dataset.
"""

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import os

import matplotlib.pyplot as plt
import seaborn as sns

# Create dir at the path passed
OUTPUT_DIR = "outputs/week2/eda"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # dont throw error if folder already exists


# load data
def load_and_inspect(dataset_name: str) -> pd.DataFrame:
    """Load seaborn dataset and print basic inspection info"""
    df = sns.load_dataset(dataset_name)
    print("Shape: ", df.shape)
    print("\nDtypes:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDescribe:\n", df.describe())
    return df


# Clean data
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Iris dataset requires minimal cleaning due to no
    missing values or duplicates."""
    print("No cleaning needed. Shape is unchanged.", df.shape)
    return df


# Summarize with groupby: return mean of each numeric grouped by species
def summarize_by_species(df: pd.DataFrame) -> pd.DataFrame:
    """Return mean of each numeric column grouped by species"""
    mean_count = df.groupby("species").mean()
    return mean_count


# Generate plots for each
def plot_distribution(df: pd.DataFrame) -> None:
    """Histogram of petal length by species.
    Setosa is clearly separated; versicolor & virginica have overlap"""
    sns.histplot(data=df, x="petal_length", hue="species", kde=True)
    plt.title("Petal Length Distribution by Species")
    plt.savefig(f"{OUTPUT_DIR}/plot1_distribution.png", bbox_inches="tight")
    plt.clf()


def plot_comparison(df: pd.DataFrame) -> None:
    """Bar chart of mean petal length by species"""
    sns.barplot(data=df, x="species", y="petal_length")
    plt.title("Petal Length Mean by Species")
    plt.savefig(f"{OUTPUT_DIR}/plot2_comparison.png", bbox_inches="tight")
    plt.clf()


def plot_relationship(df: pd.DataFrame) -> None:
    """Heatmap of correlations between numeric columns"""
    corr = df.select_dtypes("number").corr()
    sns.heatmap(data=corr, annot=True, cmap="coolwarm")
    plt.title("Petal Length Relationship by Species")
    plt.savefig(f"{OUTPUT_DIR}/plot3_relationship.png", bbox_inches="tight")
    plt.clf()


if __name__ == "__main__":
    df = load_and_inspect("iris")
    df = clean_data(df)
    summary = summarize_by_species(df)
    print("\nMean by species:\n", summary)
    plot_distribution(df)
    plot_comparison(df)
    plot_relationship(df)
    print("Plots saved to", OUTPUT_DIR)
