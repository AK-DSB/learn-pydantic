from pydantic import BaseModel


class PetCls:
    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species


class PersonCls:
    def __init__(self, *, name: str, age: float = None, pets: list[PetCls]):
        self.name = name
        self.age = age
        self.pets = pets


class Pet(BaseModel):
    name: str
    species: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    name: str
    age: float = None
    pets: list[Pet]

    class Config:
        orm_mode = True


# bones = PetCls(name='Bones', species='dog')
# orion = PetCls(name='Orion', species='cat')
bones = Pet(name='Bones', species='dog')
orion = Pet(name='Orion', species='cat')
# anna = PersonCls(name='AKW', age=18, pets=[bones, orion])
anna = Person(name='AKW', age=18, pets=[bones, orion])
anna_model = Person.from_orm(anna)
print(anna_model)
print(anna_model.dict())
print(anna_model.json())
