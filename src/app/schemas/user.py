from typing import Annotated, Required

from annotated_types import Len, MaxLen, MinLen
from pydantic import BaseModel, Field

from .form_body import form_body


@form_body
class UserForm(BaseModel):
    fname: Annotated[str, MinLen(1), MaxLen(64), Required, Field(alias="fname")]
    lname: Annotated[str, MinLen(1), MaxLen(64), Field(alias="lname", default=None)]
    phone: Annotated[
        str, Len(11), Required, Field(alias="phone", pattern=r"^[0-9]{11}$")
    ]
