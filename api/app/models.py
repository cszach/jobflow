from pydantic import BaseModel, Field, ConfigDict
from bson.objectid import ObjectId


class User(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str | None = Field(alias="_id")
    email: str
    name: str
    bio: str
