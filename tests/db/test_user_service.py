from assertpy import assert_that

from db.database import SessionLocal, engine
from db import crud, models, schemas
from sqlalchemy.orm import Session


def get_db_session():
    sl = SessionLocal()
    try:
        yield sl
    finally:
        sl.close()


def test_query_user(session: Session) -> None:
    phone: str = "14252958064"
    user = crud.get_user(session, phone)
    assert_that(user).is_not_none()
    assert_that(user.phone).is_equal_to(phone)
