from typing import Annotated, List

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import Campaign


class CampaignRepository:
    def __init__(self, session: Annotated[Session, Depends(get_db)]):
        self.session = session

    def get_by_id(self, id: int) -> Campaign | None:
        return self.session.query(Campaign).filter(Campaign.id == id).first()

    def get_all(self) -> List[Campaign]:
        return self.session.query(Campaign).all()

    def insert(self, campaign: Campaign) -> Campaign:
        self.session.add(campaign)
        self.session.commit()
        self.session.refresh(campaign)
        return campaign

    # def get_users_by_id(self, id: int) -> List[User]:
    #     return None
