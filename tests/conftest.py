from typing import Generator, TypeVar

import pytest
from app.main import app
from db import CampaignRepository, UserRepository, models
from db.database import SessionLocal, engine
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


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
    return "postgresql://postgres:postgres@localhost:5432/postgres"


@pytest.fixture
def user_repo(session: Session) -> UserRepository:
    return UserRepository(session)


@pytest.fixture
def campaign_repo(session: Session) -> CampaignRepository:
    return CampaignRepository(session)
