# commands/update_order_status_command.py

from dataclasses import dataclass


@dataclass
class UpdateOrderStatusCommand:
    order_id: int
    status: str
