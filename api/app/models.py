from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        return PydanticObjectId(v)
    
    # Implement __get_pydantic_core_schema__
    def __get_pydantic_schema__(self, model):
        return {"type": "string", "format": "objectid"}


class User(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: PydanticObjectId = Field(alias="_id")
    email: str
    name: str
    bio: str

    def to_json(self):
        return self.dict(exclude_none=True)
    
    def to_bson(self):
        return self.dict(by_alias=True, exclude_none=True)
