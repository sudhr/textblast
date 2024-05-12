from assertpy import assert_that
import string
import random
from db.models import User
from db.repo import UserRepository


def test_get_user_phone_exists(user_repo: UserRepository) -> None:
    phone: str = "14252958064"
    user = user_repo.get_by_phone(phone)
    assert_that(user).is_not_none()
    assert_that(user.phone).is_equal_to(phone)


def test_get_user_phone_does_not_exist(user_repo: UserRepository) -> None:
    phone: str = "14255551212"
    user = user_repo.get_by_phone(phone)
    assert_that(user).is_none()


def create_random_phonenumber() -> str:
    return "".join(random.choices(string.digits, k=11))


def test_add_user(user_repo: UserRepository) -> None:
    phone: str = create_random_phonenumber()
    user: User = User(fname="First", lname="Last", phone=phone)
    user_created = user_repo.insert(user)
    assert_that(user_created.phone).is_equal_to(phone)
    assert_that(user_created.id).is_greater_than(0)
