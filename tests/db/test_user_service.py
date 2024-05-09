from db.repos import UserRepository

from assertpy import assert_that

# def test_insert_user(user_repo: UserRepository) -> None:
#     user_repo.add(User(fname="testfirst", lname="testLast", phone="11234567890"))


def test_query_user(user_repo: UserRepository) -> None:
    user = user_repo.get_by_id(1)
    assert_that(user).is_not_none()
