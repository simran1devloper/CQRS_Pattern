# commands/cancel_order_handler.py


class CancelOrderHandler:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def handle(self, command):
        order = self.order_repository.cancel(command.order_id)

        return order
