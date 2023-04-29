from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'AKW'


user = User(id=123)


# user_x = User(id='123.45')


class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
print(m.dict())

