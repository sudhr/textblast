from fastapi.testclient import TestClient
import pytest
from http import HTTPStatus
from assertpy import assert_that


def test_app_valid_sms_request(client: TestClient):
    resp = client.post(
        "/webhook",
        json={
            "msisdn": "14252958064",
            "text": "Hello, World!",
            "messageID": "1234567890",
        },
    )
    assert_that(resp.status_code).is_equal_to(HTTPStatus.OK)


@pytest.mark.parametrize(
    "name,json,expected_status_code",
    [
        ("Short msisdn", {"Msisdn": "2342"}, HTTPStatus.UNPROCESSABLE_ENTITY),
        (
            "msisdn too long",
            {"Msisdn": "234215487544"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        ),
        (
            "msisdn not a valid phone number",
            {"Msisdn": "234abdwer215487544"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        ),
        ("Empty msisdn", {"Msisdn": ""}, HTTPStatus.UNPROCESSABLE_ENTITY),
        ("Missing msisdn", {"text": "something"}, HTTPStatus.UNPROCESSABLE_ENTITY),
        ("Empty text", {"text": ""}, HTTPStatus.UNPROCESSABLE_ENTITY),
        ("Empty messageID", {"messageID": ""}, HTTPStatus.UNPROCESSABLE_ENTITY),
        ("MessageID only", {"messageID": "123"}, HTTPStatus.UNPROCESSABLE_ENTITY),
        (
            "Valid messageID, missing other fields",
            {"messageID": "12345678901234567890"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        ),
    ],
)
def test_sms_request_bad_data(
    client: TestClient, name: str, json: dict, expected_status_code: HTTPStatus
):
    resp = client.post("/webhook", json=json)
    assert_that(resp.status_code).is_equal_to(expected_status_code)
