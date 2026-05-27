# queries/get_order_handler.py


class GetOrderHandler:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def handle(self, query):
        order = self.order_repository.get_by_id(query.order_id)

        return order
