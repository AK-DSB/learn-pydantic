"""
When declaring a field with a default value, 
you may want it to be dynamic (i.e. different for each model). 
To do this, you may want to use a default_factory
"""


from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


m1 = Model()
m2 = Model()
print(f'{m1.uid} != {m2.uid}')
print(f'{m1.updated} != {m2.updated}')
