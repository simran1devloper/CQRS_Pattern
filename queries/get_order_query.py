# queries/get_order_query.py

from dataclasses import dataclass


@dataclass
class GetOrderQuery:
    order_id: int
