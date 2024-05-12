from pydantic import BaseModel, Field


class SMS(BaseModel):
    """Incoming data model for webhook.

    Args:
        BaseModel (_type_): _description_
    """

    msisdn: str = Field(
        alias="msisdn", min_length=11, max_length=11, pattern="^\\d{11}$"
    )
    text: str = Field(alias="text", min_length=1, max_length=250)
    messageId: str = Field(alias="messageID", min_length=5, max_length=64)


class UserBase(BaseModel):
    id: int
    fname: str
    lname: str | None = None
    phone: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    class Config:
        orm_mode = True
        # from_attributes = ("id", "fname", "lname", "phone")

    # class ReachedBase(BaseModel):
    #     id: int
    #     user_id: int
    #     timestamp: datetime

    #     class Config:
    #         orm_mode = True

    # class ReachedCreate(ReachedBase):
    # pass
