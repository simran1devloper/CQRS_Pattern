# repositories/order_read_repository.py

from models.order import Order


class OrderReadRepository:
    def __init__(self):
        self.orders_by_id = {}

    def upsert(self, order_id: int, customer_id: int, items: list[str], status: str):
        order = Order(
            id=order_id,
            customer_id=customer_id,
            items=list(items),
            status=status
        )

        self.orders_by_id[order_id] = order
        return order

    def update_status(self, order_id: int, status: str):
        order = self.orders_by_id.get(order_id)

        if order is None:
            return None

        order.status = status
        return order

    def get_by_id(self, order_id: int):
        return self.orders_by_id.get(order_id)

    def get_by_customer_id(self, customer_id: int):
        return [
            order
            for order in self.orders_by_id.values()
            if order.customer_id == customer_id
        ]
