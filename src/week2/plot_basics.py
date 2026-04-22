"""
Week 2 Day 4 - Matplotlib Basics
Core plotting functions using the object-oriented Matplotlib API

"""

import matplotlib

matplotlib.use(
    "Agg"
)  # non-interactive backend (safe for testing) / tells matplotlib to render
import matplotlib.pyplot as plt
import numpy as np


def plot_line(x, y, title="Line Plot", xlabel="x", ylabel="y"):
    """
    Plot a line chart from x and y data.

    Parameters
    ----------
    x : array-like
        Values for the x-axis.
    y : array-like
        Values for the y-axis.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.

    Returns
    -------
    fig, ax : tuple
        The Matplotlib Figure and Axes objects.
    """
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax


def plot_bar(categories, values, title="Bar Chart", xlabel="Category", ylabel="Value"):
    """
    Plot a bar chart.

    Parameters
    ----------
    categories : array-like
        Labels for each bar.
    values : array-like
        Heights of each bar.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.

    Returns
    -------
    fig, ax : tuple
        The Matplotlib Figure and Axes objects.
    """
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax


def plot_scatter(x, y, title="Scatter Plot", xlabel="x", ylabel="y"):
    """
    Plot a scatter chart.

    Parameters
    ----------
    x : array-like
        Values for the x-axis.
    y : array-like
        Values for the y-axis.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.

    Returns
    -------
    fig, ax : tuple
        The Matplotlib Figure and Axes objects.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax


def plot_histogram(
    data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency"
):
    """
    Plot a histogram.

    Parameters
    ----------
    data : array-like
        The data to distribute into bins.
    bins : int
        Number of bins.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.

    Returns
    -------
    fig, ax : tuple
        The Matplotlib Figure and Axes objects.
    """
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax
