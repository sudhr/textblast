from pydantic import BaseModel, Field

from .form_body import form_body


@form_body
class UserForm(BaseModel):
    fname: str = Field(alias="fname", min_length=1, max_length=64, required=True)
    lname: str = Field(alias="lname", min_length=1, max_length=64)
    phone: str = Field(alias="phone", min_length=11, max_length=11, required=True)
