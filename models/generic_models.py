"""
Pydantic supports the creation of generic models to make it easier to reuse a common model structure.

In order to declare a generic model, you perform the following steps:

Declare one or more typing.TypeVar instances to use to parameterize your model.
Declare a pydantic model that inherits from pydantic.generics.GenericModel and typing.Generic, where you pass the TypeVar instances as parameters to typing.Generic.
Use the TypeVar instances as annotations where you will want to replace them with other types or pydantic models.
"""
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Error(BaseModel):
    code: int
    message: str


class DataModel(BaseModel):
    numbers: list[int]
    people: list[str]


class Response(GenericModel, Generic[DataT]):
    data: DataT | None
    error: Error | None

    @validator('error', always=True)
    def check_consistency(cls, v, values):
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return v


data = DataModel(numbers=[1, 2, 3], people=[])
error = Error(code=404, message='Not found')

print(Response)
print(Response[int](data=1))
print(Response[str](data='value'))
print(Response[DataModel](data=data))
print(Response[DataModel](data=data).dict())
print(Response[DataModel](error=error))
print(Response[DataModel](error=error).json())

try:
    Response[int](data='value')
except ValidationError as e:
    print(e)
