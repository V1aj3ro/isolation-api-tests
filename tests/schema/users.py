from pydantic import BaseModel, ConfigDict, UUID4, EmailStr
from pydantic.alias_generators import to_camel


class UserTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True
    )

    id: UUID4
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class GetUserResponseTestSchema(BaseModel):
    user: UserTestSchema
