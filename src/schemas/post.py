from pydantic import BaseModel
from datetime import datetime

class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now()
    published: bool = False
