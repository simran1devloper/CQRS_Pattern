# events/order_events.py

from dataclasses import dataclass


@dataclass
class OrderCreatedEvent:
    order_id: int
    customer_id: int
    items: list[str]
    status: str


@dataclass
class OrderStatusUpdatedEvent:
    order_id: int
    status: str


@dataclass
class OrderCancelledEvent:
    order_id: int
    status: str
