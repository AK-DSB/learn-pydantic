import pickle
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'AKW'
    signup_ts: datetime = None


m = User.parse_obj({'id': 1, 'name': 'AK'})
print(m)


try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)


m = User.parse_raw('{"id": 1, "name": "AKW"}')
print(m)


pickle_data = pickle.dumps({
    'id': 1,
    'name': 'AK',
    'signup_ts': datetime(2023, 4, 29)
})

m = User.parse_raw(
    pickle_data, content_type='application/pickle', allow_pickle=True
)
print(m)

path = Path('data.json')
path.write_text('{"id": 1, "name": "AKW"}')
m = User.parse_file(path)
print(m)
