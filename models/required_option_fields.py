"""
To declare a field as required, 
you may declare it using just an annotation, 
or you may use an ellipsis (...) as the value:
"""
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    a: int
    b: int = ...
    c: int = Field(...)


"""
If you want to specify a field that can take a None value 
while still being required, 
you can use Optional with ...
"""


class Model(BaseModel):
    a: int | None
    b: int | None = ...
    c: int | None = Field(...)


print(Model(b=1, c=2))
try:
    # Model(a=1, b=2)
    m = Model(a=1, c=2, b=None)
    print(m)
except ValidationError as e:
    print(e)
