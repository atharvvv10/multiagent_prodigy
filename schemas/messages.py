from pydantic import BaseModel

class Message(BaseModel):
    text: str
    source: str = "en"
    target: str = "fr"
 
