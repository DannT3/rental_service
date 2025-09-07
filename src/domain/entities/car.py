from dataclasses import dataclass
from domain.value_objects.car_value_objects.brand import Brand


@dataclass(frozen=True)
class Car:
    car_id: int
    brand: Brand
    





