from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# create paths for graphs to go to
OUTPUT_DIR = Path("data/output/week3")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# create a histogram to see ages of passengers
def plot_distribution(df: pd.DataFrame, column: str, save: bool = True) -> None:
    """Plot histogram & KDE for a numeric column"""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=column, bins=20, kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    if save:
        path = OUTPUT_DIR / f"dist_{column}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.show()


# build a plot to see how many passengers fell into each category
def plot_categorical_counts(df: pd.DataFrame, column: str, save: bool = True) -> None:
    """Bar char to show the categorical columns"""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(df, x=column, ax=ax)
    ax.set_title(f"Counts by {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    if save:
        path = OUTPUT_DIR / f"counts_{column}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.show()


def plot_survival_by_category(df: pd.DataFrame, column: str, save: bool = True) -> None:
    """Grouped bar chart showing survival counts within each category"""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x=column, hue="Survived", ax=ax)
    ax.set_title(f"Survival by {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    if save:
        path = OUTPUT_DIR / f"survival_{column}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, column: str, save: bool = True) -> None:
    """"""
    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = df.select_dtypes(include="number").corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title(f"Correlation Heatmap")

    if save:
        path = OUTPUT_DIR / "correlation_heatmap.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"Saved: {path}")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("data/raw/titanic.csv")
    plot_distribution(df, "Age")

    plot_categorical_counts(df, "Pclass")

    plot_survival_by_category(df, "Pclass")

    plot_correlation_heatmap(df, "Pclass")
