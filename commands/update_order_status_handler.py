# commands/update_order_status_handler.py


class UpdateOrderStatusHandler:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def handle(self, command):
        order = self.order_repository.update_status(
            order_id=command.order_id,
            status=command.status
        )

        return order
