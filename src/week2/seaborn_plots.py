"""
Week 2 Day 4 - Seaborn Plots
Statistical visualizations using Seaborn.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_distribution(data, column, title="Distribution", ax=None):
    """
    Plot the distribution of a single numeric column.

    Parameters
    ----------
    data : pd.DataFrame
        The source DataFrame.
    column : str
        Column name to plot.
    title : str
        Plot title.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on. Creates a new one if None.

    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        _, ax = plt.subplots()
    """data = the dataframe being passed
        x = the column from the dataframe to plot
        kde = kernel density estimate
        kde draws a smooth curve on top of the histogram bars
        that estimates the shape of the underlying distribution
        ax = ax tells seaborn which matplotlib axis to draw on"""
    sns.histplot(data=data, x=column, kde=True, ax=ax)
    ax.set_title(title)
    return ax
