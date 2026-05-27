# commands/cancel_order_command.py

from dataclasses import dataclass


@dataclass
class CancelOrderCommand:
    order_id: int
