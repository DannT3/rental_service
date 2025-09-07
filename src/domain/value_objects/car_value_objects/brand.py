from dataclasses import dataclass


@dataclass(frozen=True)
class Brand:
    value: str
