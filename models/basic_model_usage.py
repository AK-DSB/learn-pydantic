from pydantic import BaseModel


class User(BaseModel):
    """
    User
    """
    id: int
    name = 'AKW'


user = User(id=123)


# user_x = User(id='123.45')


class Foo(BaseModel):
    """
    Foo
    """
    count: int
    size: float | None = None


class Bar(BaseModel):
    """
    Bar
    """
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    """
    Spam
    """
    foo: Foo
    bars: list[Bar]


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
print(m.dict())
