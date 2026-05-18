import pydantic

class User(pydantic.BaseModel):
    id: int
    name: str
    email: str