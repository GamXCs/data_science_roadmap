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


def plot_boxplot(data, x, y, title="Box Plot", ax=None):
    """
    Plot a boxplot comparing a numeric variable across categories.

    Parameters
    ----------
    data : pd.DataFrame
        The source DataFrame.
    x : str
        Categorical column for the x-axis.
    y : str
        Numeric column for the y-axis.
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
    sns.boxplot(data=data, x=x, y=y, ax=ax)
    ax.set_title(title)
    return ax


def plot_heatmap(data, title="Heatmap", ax=None):
    """
    Plot a heatmap of a correlation matrix.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame of numeric columns to correlate.
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
    corr = (
        data.corr()
    )  # computes correlation matrx between numeric cols (between -1 and 1)
    sns.heatmap(
        corr, annot=True, fmt=".2f", ax=ax
    )  # annot/fmt prints corr val inside each cell
    ax.set_title(title)
    return ax


def plot_scatter_regression(data, x, y, title="Scatter with Regression", ax=None):
    """
    Plot a scatter plot with a regression line.

    Parameters
    ----------
    data : pd.DataFrame
        The source DataFrame.
    x : str
        Column name for the x-axis.
    y : str
        Column name for the y-axis.
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
    sns.regplot(data=data, x=x, y=y, ax=ax)
    ax.set_title(title)
    return ax
