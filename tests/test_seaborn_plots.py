import matplotlib
from pandas.core.dtypes.cast import NumpyArrayT

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pytest

# from matplotlib.axes import Axes
from src.week2.seaborn_plots import (
    plot_boxplot,
    plot_distribution,
    plot_heatmap,
    plot_scatter_regression,
)


# -------------- plot_distribution -------------
@pytest.fixture  # this treats the dataframe like a global var
def sample_df():
    return pd.DataFrame({"score": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})


def test_plot_distribution_returns_ax(sample_df):
    ax = plot_distribution(sample_df, "score")
    assert isinstance(ax, plt.Axes)


def test_plot_distribution_sets_title(sample_df):
    ax = plot_distribution(sample_df, "score", title="My Distribution")
    assert ax.get_title() == "My Distribution"


def test_plot_distribution_accepts_existing_ax(sample_df):
    fig, ax = plt.subplots()
    result = plot_distribution(sample_df, "score", ax=ax)
    assert result is ax


# -------------- plot_boxplots -------------
@pytest.fixture
def boxplot_df():
    return pd.DataFrame(
        {
            "subject": ["Math", "Math", "English", "English", "Science", "Science"],
            "score": [88, 92, 72, 78, 95, 89],
        }
    )


def test_boxplot_returns_ax(boxplot_df):
    ax = plot_boxplot(boxplot_df, "subject", "score")
    assert isinstance(ax, plt.Axes)


def test_boxplot_sets_title(boxplot_df):
    ax = plot_boxplot(boxplot_df, "subject", "score", title="Scores by Subject")
    assert ax.get_title() == "Scores by Subject"


def test_boxplot_accepts_existing_ax(boxplot_df):
    fig, ax = plt.subplots()
    result = plot_boxplot(boxplot_df, "subject", "score", ax=ax)
    assert result is ax


# -------------- plot_heatmap -------------
@pytest.fixture
def numeric_df():
    return pd.DataFrame(
        {
            "height": [150, 160, 170, 180, 190],
            "weight": [50, 60, 70, 80, 90],
            "age": [20, 25, 30, 35, 40],
        }
    )


# data.corr() only works with numeric cols
def test_heatmap_sets_title(numeric_df):
    ax = plot_heatmap(numeric_df, title="Heatmap")
    assert ax.get_title() == "Heatmap"


def test_heatmap_returns_ax(numeric_df):
    ax = plot_heatmap(numeric_df)
    assert isinstance(ax, plt.Axes)


def test_heatmap_accepts_existing_ax(numeric_df):
    fig, ax = plt.subplots()
    result = plot_heatmap(numeric_df, ax=ax)
    assert result is ax


# -------------- plot_scatter_regression -------------
@pytest.fixture
def regression_df():
    return pd.DataFrame(
        {"height": [150, 160, 170, 180, 190], "weight": [50, 60, 70, 80, 90]}
    )


def test_scatter_regression_returns_ax(regression_df):
    ax = plot_scatter_regression(regression_df, "height", "weight")
    assert isinstance(ax, plt.Axes)


def test_scatter_regression_sets_title(regression_df):
    ax = plot_scatter_regression(
        regression_df, "height", "weight", title="Height vs Weight"
    )
    assert ax.get_title() == "Height vs Weight"


def test_scatter_regression_accepts_existing_ax(regression_df):
    fig, ax = plt.subplots()
    result = plot_scatter_regression(regression_df, "height", "weight", ax=ax)
    assert result is ax
