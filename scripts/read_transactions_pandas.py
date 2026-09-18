import pandas as pd

from data_engineering_roadmap.database import engine


def main():
    query = """
        SELECT
            id,
            country,
            amount,
            created_at
        FROM transactions
        ORDER BY id
    """

    df = pd.read_sql(query, engine)

    print(df)

    print("\nTotal amount:")
    print(df["amount"].sum())

    print("\nAmount by country:")
    print(
        df.groupby("country", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )


if __name__ == "__main__":
    main()
