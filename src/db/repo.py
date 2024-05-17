from typing import Annotated, List

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import User


class UserRepository:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.session = session

    def get_by_phone(self, phone: str) -> User:
        return self.session.query(User).filter(User.phone == phone).first()

    def get_by_id(self, id: int) -> User:
        return self.session.query(User).filter(User.id == id).first()

    def insert(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_all(self) -> List[User]:
        return self.session.query(User).all()
