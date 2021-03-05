from pydantic import BaseModel


class EmailSchema(BaseModel):
    """Schema for Email"""
    Payload: list = [{
                     "SenderAddress": str,
                     "SenderPassword": str,
                     "ReceiverAddress": str
                     }]
