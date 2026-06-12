"""Tests for Week 2 Day 4 - Matplotlib basics."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest

from src.week2.plot_basics import (
    plot_bar,
    plot_histogram,
    plot_line,
    plot_scatter,
)


# ------------- plot_line ------------------
def test_plot_line_returns_fig_and_ax():
    x = [1, 2, 3, 4]
    y = [10, 20, 15, 25]
    fig, ax = plot_line(x, y)
    assert isinstance(fig, plt.Figure)


def test_plot_line_sets_title():
    fig, ax = plot_line([1, 2], [3, 4], title="My Title")
    assert ax.get_title() == "My Title"


def test_plot_line_sets_axis_labels():
    fig, ax = plot_line([1, 2], [3, 4], xlabel="Time", ylabel="Value")
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Value"


def test_plot_line_default_labels():
    fig, ax = plot_line([1, 2], [3, 4])
    assert ax.get_title() == "Line Plot"


# ------------ plot_bar ----------------
def test_plot_bar_returns_fig_and_ax():
    x = [1, 2, 3, 4]
    y = [10, 20, 15, 25]
    fig, ax = plot_bar(x, y)
    assert isinstance(fig, plt.Figure)


def test_plot_bar_sets_title():
    fig, ax = plot_bar([1, 2], [3, 4], title="My Title")
    assert ax.get_title() == "My Title"


def test_plot_bar_sets_axis_labels():
    fig, ax = plot_bar([1, 2], [3, 4], xlabel="Category", ylabel="Value")
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Value"


def test_plot_bar_default_labels():
    fig, ax = plot_bar([1, 2], [3, 4])
    assert ax.get_title() == "Bar Chart"


# ------------ plot_scatter ----------------
def test_plot_scatter_returns_fig_and_ax():
    x = [1, 2, 3, 4]
    y = [10, 20, 15, 25]
    fig, ax = plot_scatter(x, y)
    assert isinstance(fig, plt.Figure)


def test_plot_scatter_sets_title():
    fig, ax = plot_scatter([1, 2], [3, 4], title="Scatter Plot")
    assert ax.get_title() == "Scatter Plot"


def test_plot_scatter_sets_axis_labels():
    fig, ax = plot_scatter([1, 2], [3, 4], xlabel="x", ylabel="y")
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"


def test_plot_scatter_default_labels():
    fig, ax = plot_scatter([1, 2], [3, 4])
    assert ax.get_title() == "Scatter Plot"


# ---------- plot_histogram ---------------
def test_plot_histogram_returns_fig_and_ax():
    x = [1, 2, 3, 4]
    fig, ax = plot_histogram(x)
    assert isinstance(fig, plt.Figure)


def test_plot_histogram_sets_title():
    fig, ax = plot_histogram([1, 2, 6, 7], title="Histogram")
    assert ax.get_title() == "Histogram"


def test_plot_histogram_sets_axis_labels():
    fig, ax = plot_histogram([1, 2, 5], xlabel="Value", ylabel="Frequency")
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"


def test_plot_histogram_default_labels():
    fig, ax = plot_histogram([1, 2, 6, 9])
    assert ax.get_title() == "Histogram"


def test_plot_histogram_bin_count():
    fig, ax = plot_histogram([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], bins=5)
    assert len(ax.patches) == 5
