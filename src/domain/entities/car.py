from dataclasses import dataclass
from domain.value_objects.car_value_objects.brand import Brand
from domain.value_objects.car_value_objects.car_id import CarId
from domain.entities.entity import Entity
from domain.value_objects.car_value_objects.car_type import CarType
from domain.value_objects.car_value_objects.price import CarPrice


@dataclass(frozen=True)
class Car(Entity):
    car_id: CarId
    brand: Brand
    car_type: CarType
    price: CarPrice








