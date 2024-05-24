from datetime import datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, Field

from .form_body import form_body


@form_body
class NewCampaignForm(BaseModel):
    name: Annotated[str, MinLen(1), MaxLen(64), Field(alias="name")]
    description: Annotated[str, MaxLen(255), Field(alias="description")]
    start_time: Annotated[datetime, Field(alias="start_date")]
    end_time: Annotated[datetime, Field(alias="end_date")]
