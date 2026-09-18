from sqlalchemy import text

from data_engineering_roadmap.database import engine


def main():
    query = text(
        """
        SELECT
            id,
            country,
            amount,
            created_at
        FROM transactions
        ORDER BY id
        """
    )

    with engine.connect() as connection:
        result = connection.execute(query)

        for row in result:
            print(row)


if __name__ == "__main__":
    main()
