"""
Quick demo script to render and save all Day 4 plots.
Run from project root: python src/week2/viz_demo.py
"""

import matplotlib

matplotlib.use("Agg")
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.week2.plot_basics import plot_bar, plot_histogram, plot_line, plot_scatter
from src.week2.seaborn_plots import (
    plot_boxplot,
    plot_distribution,
    plot_heatmap,
    plot_scatter_regression,
)

# plot_scatter_regression

# Create output folder
os.makedirs("data/output/day4_plots", exist_ok=True)

# --- plot_line ---
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plot_line(x, y, title="Sine Wave", xlabel="x", ylabel="sin(x)")
fig.savefig("data/output/day4_plots/line.png")
plt.close(fig)

# --- plot_bar ---
categories = ["Math", "English", "Science", "History"]
values = [88, 72, 95, 61]
fig, ax = plot_bar(categories, values, title="Test Scores by Subject")
fig.savefig("data/output/day4_plots/bar.png")
plt.close(fig)

# --- plot_scatter ---
np.random.seed(42)
x = np.random.randn(50)
y = x * 2 + np.random.randn(50)
fig, ax = plot_scatter(x, y, title="Random Scatter", xlabel="x", ylabel="y")
fig.savefig("data/output/day4_plots/scatter.png")
plt.close(fig)

# --- plot_histogram ---
data = np.random.normal(loc=70, scale=10, size=200)
fig, ax = plot_histogram(data, bins=20, title="Test Score Distribution")
fig.savefig("data/output/day4_plots/histogram.png")
plt.close(fig)

# --- plot_distribution ---
df = pd.DataFrame({"score": np.random.normal(70, 10, 200)})
ax = plot_distribution(df, "score", title="Score Distribution (KDE)")
ax.get_figure().savefig("data/output/day4_plots/distribution.png")
plt.close("all")

# --- plot_scatter_regression ---
df2 = pd.DataFrame(
    {"height": np.random.normal(170, 10, 50), "weight": np.random.normal(70, 15, 50)}
)
ax = plot_scatter_regression(df2, "height", "weight", title="Height vs Weight")
ax.get_figure().savefig("data/output/day4_plots/scatter_regression.png")
plt.close("all")

# ------ plot_boxplot --------
df1 = pd.DataFrame(
    {
        "subject": ["Math", "Math", "English", "English", "Science", "Science"],
        "score": [88, 92, 72, 78, 95, 89],
    }
)
ax = plot_boxplot(df1, x="subject", y="score", title="Box Plot")
ax.get_figure().savefig("data/output/day4_plots/boxplot.png")
plt.close("all")

# ---- plot_heatmap ------
df2 = pd.DataFrame(
    {
        "height": [150, 160, 170, 180, 190],
        "weight": [50, 60, 70, 80, 90],
        "age": [20, 25, 30, 35, 40],
    }
)

ax = plot_heatmap(df2, title="Heatmap")
ax.get_figure().savefig("data/output/day4_plots/heatmap.png")

print("All plots saved to data/output/day4_plots/")
