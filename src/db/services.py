from datetime import datetime
from db.repos import ReachedRepository, UserRepository


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def get_by_id(self, user_id):
        return self._repo.get_by_id(user_id)


class ReachedService:
    def __init__(self, repo: ReachedRepository) -> None:
        self._repo = repo

    def add(self, user_id):
        return self._repo.add(user_id, timestamp=datetime.now())
