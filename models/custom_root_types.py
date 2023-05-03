import json
from pydantic import BaseModel, ValidationError
from pydantic.schema import schema


class Pets(BaseModel):
    __root__: list[str]


print(Pets(__root__=['dog', 'cat']))
print(Pets(__root__=['dog', 'cat']).json())
print(Pets.parse_obj(['dog', 'cat']))
print(Pets.schema())

pets_schema = schema([Pets])
print(json.dumps(pets_schema, indent=2))

print(Pets.parse_obj({'__root__': ['dog', 'cat']}))  # not recommended


class PetsByName(BaseModel):
    __root__: dict[str, str]


print(PetsByName.parse_obj({'Otis': 'dog', 'Milo': 'cat'}))

try:
    PetsByName.parse_obj({'__root__': {'Otis': 'dog', 'Milo': 'cat'}})
except ValidationError as e:
    print(e)
