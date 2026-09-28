import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Format attendu : postgresql://utilisateur:motdepasse@localhost:5432/nom_base
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/todo_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Fournit une session DB à chaque requête, puis la ferme automatiquement."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
