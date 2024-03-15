from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def create_database_connection(username, password, host, database):
    try:
        print(f'Connected to the MySQL Database at {host}')
        engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')
        connection = engine.connect()
        Session = sessionmaker(connection)
        print("Connected to database")
        return Session
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

class DatabaseConnector:
    def __init__(self, Session):
        self.Session = Session

    def get_session(self):
        return self.Session

username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_URL")
database = os.getenv("DATABASE_NAME")

# Create database connection
Session = create_database_connection(username, password, host, database)

# Initialize database connector
db_connector = DatabaseConnector(Session)

# Example usage
session = db_connector.get_session()
