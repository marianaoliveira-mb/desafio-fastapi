from pydantic import BaseModel, Field, NonNegativeInt
from datetime import datetime

class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
    completed: bool = False
    created_date: datetime = datetime.now()

class NoteDB(NoteSchema):
    id: int
    