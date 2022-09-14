import typing
import orjson
import dataclasses

@dataclasses.dataclass
class Member:
    id: int
    active: bool = dataclasses.field(default=False)

@dataclasses.dataclass
class Object:
    id: int
    name: str
    members: typing.List[Member]


if __name__ == "__main__":
    j_son = orjson.dumps(Object(1,'name', [Member(1,True), Member(2,False)]))
    print(j_son)
    