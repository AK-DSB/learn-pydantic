from pydantic import BaseModel
from typing import Any, AnyStr
from pydantic.utils import GetterDict
from xml.etree.ElementTree import fromstring


xmlstring = """
<User Id="2138" Status="1">
    <FirstName Value="AKW" />
    <LastName Value="AKW" />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):

    def get(self, key: str, default: Any) -> Any:
        print('key--->', key)
        if key in {'Id', 'Status'}:
            # element attributes
            return self._obj.attrib.get(key, default)

        # element children
        try:
            return self._obj.find(key).attrib['Value']
        except (AttributeError, KeyError):
            return default


class User(BaseModel):
    Id: int
    Status: str | None
    FirstName: str | None
    LastName: str | None
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter


print(fromstring(xmlstring))
user = User.from_orm(fromstring(xmlstring))
print(user)
