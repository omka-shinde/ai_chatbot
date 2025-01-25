# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these with your actual database credentials:
DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"  # For MySQL
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost/dbname"  # For PostgreSQL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Base class for models (you will define your models based on this)
Base = declarative_base()

# Create a session maker for interacting with the database
Session = sessionmaker(bind=engine)

def get_session():
    """
    Get a new session for querying the database.
    """
    return Session()

def create_all_tables():
    """
    Create all tables defined in the SQLAlchemy models.
    """
    Base.metadata.create_all(engine)
