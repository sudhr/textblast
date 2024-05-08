from fastapi.testclient import TestClient
import pytest

from webhook import app


@pytest.fixture
def client():
    return TestClient(app)
