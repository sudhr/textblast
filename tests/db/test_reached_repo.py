from assertpy import assert_that
from db.models import User, Reached
from db.repo import UserRepository, ReachedRepository


def phone() -> str:
    # return "14252958064"
    return "49627617817"


def test_insert(reached_repo: ReachedRepository, user_repo: UserRepository) -> None:
    user = user_repo.get_by_phone(phone())
    assert_that(user).is_not_none()
    assert_that(user.id).is_greater_than(0)
    reached = reached_repo.insert(user.id)
    assert_that(reached).is_not_none()
    assert_that(reached.id).is_greater_than(0)
    assert_that(reached.timestamp).is_not_none()
