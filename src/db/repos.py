from contextlib import AbstractContextManager
import datetime
from typing import Callable
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import User, Reached


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def get_by_id(self, user_id: int) -> User:
        with self._session_factory() as session:
            stmt = select(User).where(User.id == user_id)
            return session.scalars(stmt).one()


class ReachedRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def add(self, user_id: int, ts: datetime) -> Reached:
        with self._session_factory() as session:
            row = Reached(user_id=user_id, timestamp=ts)
            session.add(row)
            session.commit()
            session.refresh(row)
            return row
