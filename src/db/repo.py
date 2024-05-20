from typing import Annotated, List

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import Campaign, User


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


class CampaignRepository:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.session = session

    def get_by_id(self, id: int) -> Campaign:
        return self.session.query(Campaign).filter(Campaign.id == id).first()

    def get_all(self) -> List[Campaign]:
        return self.session.query(Campaign).all()

    def insert(self, campaign: Campaign) -> Campaign:
        self.session.add(campaign)
        self.session.commit()
        self.session.refresh(campaign)
        return campaign

    def get_users_by_id(self, id: int) -> List[User]:
        pass
