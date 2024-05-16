import logging
from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# from .models import models

# SQLALCHEMY_DATABASE_URL = "sqlite:///./data/db.sqlite3"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"


logger = logging.getLogger(__name__)

engine = create_engine(
    #    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    # for Postgres
    SQLALCHEMY_DATABASE_URL,
    isolation_level="SERIALIZABLE",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# models.Base.metadata.create_all(bind=engine)

Base = declarative_base()


def get_db() -> Generator[Session, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
