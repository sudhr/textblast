import pytest
from typing import Generator, TypeVar
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine
from db import models
from db.repo import ReachedRepository, UserRepository
from webhook import app


@pytest.fixture
def client():
    return TestClient(app)


T = TypeVar("T")
YieldFixture = Generator[T, None, None]

#
# Database fixtures
#

models.Base.metadata.create_all(bind=engine)


@pytest.fixture
def session() -> YieldFixture[Session]:
    sl = SessionLocal()
    with sl as session:
        yield session


@pytest.fixture
def db_conn_string() -> str:
    return "sqlite:///./data/db.sqlite3"


@pytest.fixture
def user_repo(session: Session) -> UserRepository:
    return UserRepository(session)


@pytest.fixture
def reached_repo(session: Session) -> ReachedRepository:
    return ReachedRepository(session)