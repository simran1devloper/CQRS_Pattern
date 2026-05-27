# repositories/order_write_repository.py

from models.order import Order


class OrderWriteRepository:
    def __init__(self):
        self.orders = []
        self.current_id = 1

    def save(self, customer_id: int, items: list[str]):
        order = Order(
            id=self.current_id,
            customer_id=customer_id,
            items=items,
            status="CREATED"
        )

        self.orders.append(order)
        self.current_id += 1

        return order

    def get_by_id(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                return order

        return None

    def update_status(self, order_id: int, status: str):
        order = self.get_by_id(order_id)

        if order is None:
            return None

        order.status = status
        return order

    def cancel(self, order_id: int):
        return self.update_status(order_id, "CANCELLED")
