from dataclasses import asdict, dataclass


@dataclass
class DTO:
    # This values will be assined to base_ if its None
    values = []

    def asdict(self) -> dict:
        return {"entity": asdict(self)}

    def __post_init__(self):
        self.init_base()

    def init_base(self) -> None:
        for value_name in self.values:
            exec(
                f"self.base_{value_name} = self.{value_name} if self.base_{value_name} is None else self.base_{value_name}"
            )
