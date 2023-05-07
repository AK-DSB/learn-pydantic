"""
pydantic may cast input data to force it to conform 
to model field types, 
and in some cases this may result in a loss of information.
"""
import inspect
from pydantic import BaseModel, Field


class Model(BaseModel):
    a: int
    b: float
    c: str


print(Model(a=3.1415, b=' 2.72', c=123))
print(Model(a=3.1415, b=' 2.72', c=123).dict())


# ModelSignature

"""
All pydantic models will have 
their signature generated based on their fields:
"""


class FooModel(BaseModel):
    id: int
    name: str = None
    description: str = 'Foo'
    apple: int = Field(..., alias='pear')


print(inspect.signature(FooModel))


class MyModel(BaseModel):
    id: int
    info: str = 'Foo'

    def __init__(self, id: int = 1, *, bar: str, **data) -> None:
        """My custom init!"""
        super().__init__(id=id, bar=bar, **data)


print(inspect.signature(MyModel))


# Structural pattern matching

"""
pydantic supports structural pattern matching for models, 
as introduced by PEP 636 in Python 3.10
"""


class Pet(BaseModel):
    name: str
    species: str


a = Pet(name='Bones', species='dog')

match a:
    # match `species` to 'dog', declare and initialize `dog_name`
    case Pet(species='dog', name=dog_name):
        print(f'{dog_name} is a dog')
        # > Bones is a dog
    # default case
    case _:
        print('No dog matched')
