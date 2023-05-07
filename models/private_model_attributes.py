from datetime import datetime
from random import randint
from typing import ClassVar

from pydantic import BaseModel, PrivateAttr

"""
If you need to vary or manipulate internal attributes 
on instances of the model, you can declare them using PrivateAttr
"""


class TimeAwareModel(BaseModel):
    _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
    _secret_value: str = PrivateAttr()
    _a: int = 1

    def __init__(self, **data):
        super().__init__(**data)
        # this could also be done with default_factory
        self._secret_value = randint(1, 5)


m = TimeAwareModel()
print(m._secret_value)
print(m._processed_at)
print(m._a)

"""
If Config.underscore_attrs_are_private is True, 
any non-ClassVar underscore attribute will be treated as private
"""


class Model(BaseModel):
    _class_var: ClassVar[str] = 'class var value'
    _private_attr: str = 'private attr value'

    class Config:
        underscore_attrs_are_private = True


print(Model._class_var)
print(Model._private_attr)
print(Model()._private_attr)
