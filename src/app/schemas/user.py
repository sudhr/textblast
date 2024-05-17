from pydantic import BaseModel, Field


class User(BaseModel):
    """Incoming data model for adding user

    Args:
        BaseModel (User): Data model for add user form post.
    """

    phone: str = Field(alias="phone", min_length=11, max_length=11, required=True)
    fname: str = Field(alias="fname", min_length=1, max_length=64, required=True)
    lname: str = Field(alias="lname", min_length=1, max_length=64)
