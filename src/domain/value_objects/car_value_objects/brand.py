from dataclasses import dataclass


class EmptyBrandValue:
    pass


@dataclass(frozen=True)
class Brand:
    value: str

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyBrandValue()


