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


if __name__ == "__main__":
    df = pd.read_csv("data/raw/titanic.csv")
    plot_distribution(df, "Age")
