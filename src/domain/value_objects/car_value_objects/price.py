from dataclasses import dataclass


class NullPriceValue:
    pass


@dataclass
class CarPrice:
    value: int

    def _validate(self) -> None:
        if self.value == 0:
            raise NullPriceValue

