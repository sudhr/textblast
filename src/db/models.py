from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, name="id", primary_key=True, index=True)
    fname = Column(String, name="fname")
    lname = Column(String, name="lname")
    phone = Column(String, name="phone")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, fname={self.fname}, lname={self.lname}, phone={self.phone})>"
