import pytest
from assertpy import assert_that


def test_sms_callback():
    pass


def test_webhook(client):
    resp = client.post(
        "/webhook", json={"msisdn": "11234567890", "text": "Hello, World!"}
    )
    assert_that(resp.status_code).is_equal_to(200)
