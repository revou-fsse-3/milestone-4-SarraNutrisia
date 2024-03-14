from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_URL")
database = os.getenv("DATABASE_NAME")


try:
    print(f'Connected to the MySQL Database at {host}')
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

    connection = engine.connect()
    Session = sessionmaker(connection)

    print("Connected to database")

except Exception as e:
    print(f"Error connecting to database: {e}")