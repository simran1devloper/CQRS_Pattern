# commands/create_order_handler.py

from events.order_events import OrderCreatedEvent


class CreateOrderHandler:
    def __init__(self, order_write_repository, event_bus):
        self.order_write_repository = order_write_repository
        self.event_bus = event_bus

    def handle(self, command):
        order = self.order_write_repository.save(
            customer_id=command.customer_id,
            items=command.items
        )

        event = OrderCreatedEvent(
            order_id=order.id,
            customer_id=order.customer_id,
            items=order.items,
            status=order.status
        )
        self.event_bus.publish(event)

        return order
