from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    content: str
    user: str

class DocumentUpdate(BaseModel):
    content: str
    user: str

class TitleUpdate(BaseModel):
    title: str