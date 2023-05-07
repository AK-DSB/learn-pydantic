from pydantic import BaseModel, parse_obj_as


class Item(BaseModel):
    id: int
    name: str


item_data = [{'id': 1, 'name': 'AKW'}, {'id': 2, 'name': 'AK'}]
items = parse_obj_as(list[Item], item_data)
print(items)
