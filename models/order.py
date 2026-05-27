# models/order.py

from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_id: int
    items: list[str]
    status: str
