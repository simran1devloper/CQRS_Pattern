# commands/create_order_command.py

from dataclasses import dataclass


@dataclass
class CreateOrderCommand:
    customer_id: int
    items: list[str]
