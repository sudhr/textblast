from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, name="id", primary_key=True, index=True)
    fname = Column(String, name="fname")
    lname = Column(String, name="lname")
    phone = Column(String, name="phone")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, fname={self.fname}, lname={self.lname}, phone={self.phone})>"


class Reached(Base):
    __tablename__ = "Reached"
    id = Column(Integer, name="id", primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="Reached")
    timestamp = Column(DateTime, name="timestamp")

    def __repor__(self) -> str:
        return f"<Reached(id={self.id}, user_id={self.user_id}, timestamp={self.timestamp})>"
