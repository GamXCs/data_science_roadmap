import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pytest

from src.week2.seaborn_plots import plot_distribution


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
