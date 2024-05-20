from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, name="id", primary_key=True, index=True)
    fname = Column(String, name="fname")
    lname = Column(String, name="lname")
    phone = Column(String, name="phone")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, fname={self.fname}, lname={self.lname}, phone={self.phone})>"


campaign_user_table = Table(
    "campaign_user",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("campaign_id", ForeignKey("campaign.id")),
    Column("user_id", ForeignKey("user.id")),
)


class Campaign(Base):
    __tablename__ = "campaign"
    # id = Column(Integer, name="id", primary_key=True, index=True)
    # name = Column(String, name="name", nullable=False)
    # description = Column(String, name="description")
    # start_time = Column(String, name="start_time", nullable=False)
    # end_time = Column(String, name="end_time", nullable=False)

    id: Mapped[int] = mapped_column(Integer, name="id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, name="name", nullable=False)
    description: Mapped[str] = mapped_column(String, name="description")
    # start_time: Mapped[datetime] = mapped_column(
    #     DateTime, name="start_time", nullable=False
    # )
    # end_time: Mapped[datetime] = mapped_column(
    #     DateTime, name="end_time", nullable=False
    # )

    users: Mapped[List[User]] = relationship(
        secondary=campaign_user_table, lazy="joined"
    )

    def __repr__(self) -> str:
        return f"<Campaign(id={self.id}, name={self.name}, start_time={self.start_time}, end_time={self.end_time})>"


# class CampaignUser(Base):
#     __tablename__ = "campaign_user"
#     # id = Column(Integer, name="id", primary_key=True, index=True)
#     id = mapped_column(Integer, name="id", primary_key=True, index=True)
#     campaign_id = mapped_column(
#         Integer, ForeignKey("campaign.id"), name="campaign_id", nullable=False
#     )
#     user_id = mapped_column(
#         Integer, ForeignKey("user.id"), name="user_id", nullable=False
#     )
#     user = relationship("User")
#     campaign = relationship("Campaign")

#     def __repr__(self) -> str:
#         return f"<CampaignUser(id={self.id}, campaign_id={self.campaign_id}, user_id={self.user_id})>"
