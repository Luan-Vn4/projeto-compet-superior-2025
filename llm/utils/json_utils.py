from abc import ABC
import json
from dataclasses import asdict, dataclass
from typing import TypeVar, Type
from dacite import from_dict

T = TypeVar('T')

@dataclass(frozen=True)
class JsonSerializable(ABC):

    def to_json(self):
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    @classmethod
    def from_json(cls: Type[T], json_content: str | dict) -> T:
        if type(json_content) is str: json_content = json.loads(json_content)
        return from_dict(data_class=cls, data=json_content)
