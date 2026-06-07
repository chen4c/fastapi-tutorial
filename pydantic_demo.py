from datetime import datetime

from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = "John Doe"
    singup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "singup_ts": "2024-06-01 12:22",
    "tastes": {"wine": 9, b"cheese": 7, "cabbage": "1"},
}

user = User(**external_data)
print(user.id)
print(user.model_dump())

# continuing the above example...

from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {"id": "not an int", "tastes": {}}

try:
    User(**external_data)
except ValidationError as e:
    print(e.errors())
    """
    [
      {
          'type': 'int_parsing',
          'loc': ('id',),
          'msg': 'Input should be a valid integer, unable to parse string as an integer',
          'input': 'not an int',
          'url': 'https://errors.pydantic.dev/2/v/int_parsing',
      },
      {
          'type': 'missing',
          'loc': ('signup_ts',),
          'msg': 'Field required',
          'input': {'id': 'not an int', 'tastes': {}},
          'url': 'https://errors.pydantic.dev/2/v/missing',
      },
    ]
    """
