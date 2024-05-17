from dataclasses import dataclass
from pydantic import BaseModel, Field
from fastapi import Form


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


@form_body
class UserForm(BaseModel):
    fname: str = Field(alias="fname", min_length=1, max_length=64, required=True)
    lname: str = Field(alias="lname", min_length=1, max_length=64)
    phone: str = Field(alias="phone", min_length=11, max_length=11, required=True)
