from pathlib import Path

import pandas as pd

from src.week3.stats import (
    correlation_with_target,
    detect_outliers,
    get_skewed_columns,
    summarize_numeric,
    survival_rate_by_group,
)
from src.week3.visualize import (
    plot_categorical_counts,
    plot_correlation_heatmap,
    plot_distribution,
    plot_pairplot,
    plot_survival_by_category,
)

# path to titanic dataset
DATA_PATH = Path("data/raw/titanic.csv")


# function to load data
def load_data() -> pd.DataFrame:
    """Load and do basic inspection of Titanic dataset"""
    df = pd.read_csv(DATA_PATH)
    print(f"Shape: {df.shape}")
    print(f"\nMissing Values: \n{df.isnull().sum()}")
    print(f"\nDtypes:\n{df.dtypes}")
    return df


def run_stats(df: pd.DataFrame) -> None:
    """Run descriptive stats and print key findings."""
    print("\n----Descriptive Stats----")
    print(summarize_numeric(df))
    print(f"\nSkewed Columns: {get_skewed_columns(df)}")
    print(f"\nDetected Outliers:\n {detect_outliers(df)}")


def run_visualizations(df: pd.DataFrame) -> None:
    """Generate and save all plots"""
    print("\n----Visualizations----")
    plot_categorical_counts(df, "Sex")
    plot_categorical_counts(df, "Pclass")
    plot_categorical_counts(df, "Embarked")
    plot_correlation_heatmap(df)
    plot_distribution(df, "Age")
    plot_distribution(df, "Fare")
    plot_pairplot(df, ["Age", "Fare", "Pclass", "Survived"])
    plot_survival_by_category(df, "Sex")
    plot_survival_by_category(df, "Pclass")


def run_survival_analysis(df: pd.DataFrame) -> None:
    """Print survival rates by key groups"""
    print("\n----Survival Analysis----")
    print(survival_rate_by_group(df, "Sex"))
    print(survival_rate_by_group(df, "Pclass"))
    print(survival_rate_by_group(df, "Embarked"))
    print(correlation_with_target(df))


if __name__ == "__main__":
    df = load_data()
    print(run_stats(df))
    run_visualizations(df)
    run_survival_analysis(df)
    print("\n---- Key Findings ----")
    print("- 38% of passengers survived overall")
    print("- Women survived at 74% vs men at 19%")
    print("- 1st class survived at 63% vs 3rd class at 24%")
    print("- Fare and Pclass are the strongest numeric predictors of survival")
    print("- Age (177) and Cabin (687) have significant missing values")
