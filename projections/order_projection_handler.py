# projections/order_projection_handler.py

from events.order_events import (
    OrderCancelledEvent,
    OrderCreatedEvent,
    OrderStatusUpdatedEvent,
)


class OrderProjectionHandler:
    def __init__(self, order_read_repository):
        self.order_read_repository = order_read_repository

    def handle(self, event):
        if isinstance(event, OrderCreatedEvent):
            return self.order_read_repository.upsert(
                order_id=event.order_id,
                customer_id=event.customer_id,
                items=event.items,
                status=event.status
            )

        if isinstance(event, OrderStatusUpdatedEvent):
            return self.order_read_repository.update_status(
                order_id=event.order_id,
                status=event.status
            )

        if isinstance(event, OrderCancelledEvent):
            return self.order_read_repository.update_status(
                order_id=event.order_id,
                status=event.status
            )

        return None
