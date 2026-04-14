import numpy as np
import pandas as pd


def create_series(data: list, index: list) -> pd.Series:
    """Create a Pandas Series from a list with a custom index"""
    return pd.Series(data, index=index)


def create_dataframe(data: dict) -> pd.DataFrame:
    """Create a DataFrame from a dictionary of lists."""
    return pd.DataFrame(data)


def select_column(df: pd.DataFrame, column: str) -> pd.Series:
    """Select a single column from a DataFrame by name."""
    return df[column]


def select_row_by_label(df: pd.DataFrame, label) -> pd.Series:
    """Select a single row by index label using .loc"""
    return df.loc[label]


def select_row_by_position(df: pd.DataFrame, position: int) -> pd.Series:
    """Select a single row by integer position using .iloc"""
    return df.iloc[position]


def filter_rows(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """Return rows where the given column matches the value."""
    return df[df[column] == value]


def add_column(df: pd.DataFrame, column: str, values: list) -> pd.DataFrame:
    """Add a new column to a Dataframe"""
    df[column] = values
    return df


def drop_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Drop a column from a Dataframe"""
    return df.drop(columns=[column])


if __name__ == "__main__":
    # test create_series func
    s = create_series([10, 20, 30], ["a", "b", "c"])
    print(s)

    # test create_dataframe func
    t = create_dataframe(
        {"name": ["Alice", "Bob"], "age": [25, 30], "job": ["Student", "Teacher"]}
    )
    print(t)
    print("-" * 15)
    # test select_column
    df = pd.DataFrame(
        {"name": ["Alice", "Bob"], "age": [25, 30], "job": ["Student", "Teacher"]}
    )
    test = select_column(df, "job")
    print(test)

    # test select_by_row
    print("-" * 15)

    tester = select_row_by_label(df, 0)
    print(tester)

    # test select_row_by_position
    print("-" * 15)

    test2 = select_row_by_position(df, 1)
    print(test2)

    # test filter_rows
    print("-" * 15)
    df1 = create_dataframe({"name": ["Alice", "Bob", "Carol"], "age": [25, 30, 25]})
    result = filter_rows(df1, "age", 25)
    print(result)
