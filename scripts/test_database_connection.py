from sqlalchemy import text

from data_engineering_roadmap.database import engine


def main():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        value = result.scalar_one()

    print(f"Database connection successful: {value}")


if __name__ == "__main__":
    main()
