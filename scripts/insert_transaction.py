from sqlalchemy import text

from data_engineering_roadmap.database import engine


def main():
    query = text(
        """
        INSERT INTO transactions (country, amount)
        VALUES (:country, :amount)
        """
    )

    transaction = {
        "country": "Chile",
        "amount": 975.25,
    }

    with engine.begin() as connection:
        connection.execute(query, transaction)

    print("Transaction inserted successfully.")


if __name__ == "__main__":
    main()
