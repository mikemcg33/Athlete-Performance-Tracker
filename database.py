from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database file (you can change the name if you want)
SQLALCHEMY_DATABASE_URL = "sqlite:///./training.db"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)