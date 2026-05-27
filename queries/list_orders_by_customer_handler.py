# queries/list_orders_by_customer_handler.py


class ListOrdersByCustomerHandler:
    def __init__(self, order_read_repository):
        self.order_read_repository = order_read_repository

    def handle(self, query):
        orders = self.order_read_repository.get_by_customer_id(query.customer_id)

        return orders
