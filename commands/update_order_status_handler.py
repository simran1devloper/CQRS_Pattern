# commands/update_order_status_handler.py

from events.order_events import OrderStatusUpdatedEvent


class UpdateOrderStatusHandler:
    def __init__(self, order_write_repository, event_bus):
        self.order_write_repository = order_write_repository
        self.event_bus = event_bus

    def handle(self, command):
        order = self.order_write_repository.update_status(
            order_id=command.order_id,
            status=command.status
        )

        if order is None:
            return None

        event = OrderStatusUpdatedEvent(
            order_id=order.id,
            status=order.status
        )
        self.event_bus.publish(event)

        return order
