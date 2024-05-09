from contextlib import AbstractContextManager
from typing import Callable
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest

from db.database import Database
from db.repos import UserRepository
from db.services import UserService
from webhook import app


@pytest.fixture
def client():
    return TestClient(app)


#
# Database fixtures
#


@pytest.fixture
def db_conn_string() -> str:
    return "sqlite:///./data/db.sqlite3"
