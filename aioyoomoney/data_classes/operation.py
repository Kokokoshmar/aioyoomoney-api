from datetime import datetime as dt
from dataclasses import dataclass


@dataclass
class Operation:
    operation_id: str | None
    status: str | None
    datetime: dt | None
    title: str | None
    pattern_id: str | None
    direction: str | None
    amount: float | None
    label: str | None
    type: str | None