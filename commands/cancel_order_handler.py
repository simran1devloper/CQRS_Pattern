# commands/cancel_order_handler.py

from events.order_events import OrderCancelledEvent


class CancelOrderHandler:
    def __init__(self, order_write_repository, event_bus):
        self.order_write_repository = order_write_repository
        self.event_bus = event_bus

    def handle(self, command):
        order = self.order_write_repository.cancel(command.order_id)

        if order is None:
            return None

        event = OrderCancelledEvent(
            order_id=order.id,
            status=order.status
        )
        self.event_bus.publish(event)

        return order
