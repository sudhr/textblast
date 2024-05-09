from pydantic import BaseModel


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
