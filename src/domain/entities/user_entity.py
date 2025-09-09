from dataclasses import dataclass
from entities.base_entity import Entity


@dataclass
class User(Entity):
    full_name: str
    role: str
    email: str
    password: str
    