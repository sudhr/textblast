from sqlalchemy.orm import Session
from . import models, schemas


def get_user(s: Session, phone: str) -> models.User:
    return s.query(models.User).filter(models.User.phone == phone).first()


def create_readched(s: Session, user: schemas.User) -> None:
    s.add(models.Reached(user_id=user.id))
    s.commit()
