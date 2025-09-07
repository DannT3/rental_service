from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CarId:
    car_id: UUID