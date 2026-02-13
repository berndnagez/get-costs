from dataclasses import dataclass
from typing import Optional


@dataclass
class Refund:
    staff_id: str
    name: str
    month: Optional[str] = None
    levy_type: str = ""
    last_day: Optional[str] = None
    refunds_start_day: str = ""
    refunds_end_day: str = ""
    data_id: Optional[str] = None
    data_transfer_day: str = ""
    refund_amount: str = ""
    status: Optional[str] = None
