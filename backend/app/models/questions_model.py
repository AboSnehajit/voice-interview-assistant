from pydantic import BaseModel

class Questions(BaseModel):
    role: str
    question:str
    difficulty:str