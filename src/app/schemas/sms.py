from pydantic import BaseModel, Field

#
# Allowed phone number formats:
# * +14255551212
# * (425)555-1212
# * 4255551212
# * 425-555-1212
# * 425.555.1212
# * 425 555 1212
#


class SMS(BaseModel):
    """Incoming data model for webhook.

    Args:
        BaseModel (_type_): _description_
    """

    phone: str = Field(alias="msisdn", min_length=11, max_length=11)
    text: str = Field(alias="text", min_length=1, max_length=250)
    messageId: str = Field(alias="messageID", min_length=5, max_length=64)
