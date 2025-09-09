from dataclasses import dataclass


MAX_BRAND_LENGTH = 40

class EmptyBrandValue:
    pass


@dataclass(frozen=True)
class Brand:
    value: str

    def _validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyBrandValue()
        
    def __str__(self) -> str:
        return f"Brand:{self.value}"





