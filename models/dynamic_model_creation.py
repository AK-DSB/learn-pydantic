from pydantic import BaseModel, ValidationError, create_model, validator


"""
There are some occasions where the shape of a model is not known 
until runtime. For this pydantic provides
the create_model method to allow models to be created on the fly.

Here StaticFoobarModel and DynamicFoobarModel are identical.
"""
DynamicFoobarModel = create_model(
    'DynamicFoobarModel', foo=(str, ...), bar=123)


class StaticFoobarModel(BaseModel):
    foo: str
    bar: int = 123


class FooModel(BaseModel):
    foo: str
    bar: int = 123


BarModel = create_model(
    'BarModel',
    apple='runsset',
    banana='yellow',
    __base__=FooModel
)

print(BarModel)
print(BarModel.__fields__)


def username_alphanumeric(cls, v):
    assert v.isalnum(), 'must be alphanumeric'
    return v


validators = {
    'username_validator': validator('username')(username_alphanumeric)
}


UserModel = create_model(
    'UserModel',
    username=(str, ...),
    __validators__=validators
)

user = UserModel(username='AKW')
print(user)

try:
    UserModel(username='akw@')
except ValidationError as e:
    print(e)
