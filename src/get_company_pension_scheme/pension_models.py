from dataclasses import dataclass


@dataclass
class Pension:
    staff_id: int
    name: str
    month: str
    pension_amount: float
