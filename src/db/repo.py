from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import User, Reached


class UserRepository:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.session = session

    def get_by_phone(self, phone):
        return self.session.query(User).filter(User.phone == phone).first()

    def insert(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user


class ReachedRepository:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.session = session

    def insert(self, user: User) -> None:
        reached = Reached(user_id=user, timestamp=datetime.utcnow())
        self.session.add(reached)
        self.session.commit()
        self.session.refresh(reached)
        return reached
