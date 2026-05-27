# queries/list_orders_by_customer_query.py

from dataclasses import dataclass


@dataclass
class ListOrdersByCustomerQuery:
    customer_id: int
