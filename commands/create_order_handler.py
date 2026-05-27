# commands/create_order_handler.py


class CreateOrderHandler:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def handle(self, command):
        order = self.order_repository.save(
            customer_id=command.customer_id,
            items=command.items
        )

        return order
