# main.py

from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from infrastructure.event_bus import EventBus
from infrastructure.message_broker import InMemoryMessageBroker
from projections.order_projection_handler import OrderProjectionHandler
from repositories.order_read_repository import OrderReadRepository
from repositories.order_write_repository import OrderWriteRepository

from commands.cancel_order_command import CancelOrderCommand
from commands.cancel_order_handler import CancelOrderHandler
from commands.create_order_command import CreateOrderCommand
from commands.create_order_handler import CreateOrderHandler
from commands.update_order_status_command import UpdateOrderStatusCommand
from commands.update_order_status_handler import UpdateOrderStatusHandler

from queries.get_order_query import GetOrderQuery
from queries.get_order_handler import GetOrderHandler
from queries.list_orders_by_customer_query import ListOrdersByCustomerQuery
from queries.list_orders_by_customer_handler import ListOrdersByCustomerHandler


app = FastAPI(title="Order Management CQRS API")

message_broker = InMemoryMessageBroker()
event_bus = EventBus(message_broker)

order_write_repository = OrderWriteRepository()
order_read_repository = OrderReadRepository()

order_projection_handler = OrderProjectionHandler(order_read_repository)
event_bus.subscribe(order_projection_handler.handle)

OrderStatus = Literal["CREATED", "CONFIRMED", "SHIPPED", "DELIVERED", "CANCELLED"]


class CreateOrderRequest(BaseModel):
    customer_id: int
    items: list[str] = Field(min_length=1)


class UpdateOrderStatusRequest(BaseModel):
    status: OrderStatus


@app.post("/orders")
def create_order(request: CreateOrderRequest):
    command = CreateOrderCommand(
        customer_id=request.customer_id,
        items=request.items
    )

    handler = CreateOrderHandler(order_write_repository, event_bus)
    order = handler.handle(command)

    return {
        "message": "Order created successfully",
        "order": order
    }


@app.patch("/orders/{order_id}/status")
def update_order_status(order_id: int, request: UpdateOrderStatusRequest):
    command = UpdateOrderStatusCommand(
        order_id=order_id,
        status=request.status
    )

    handler = UpdateOrderStatusHandler(order_write_repository, event_bus)
    order = handler.handle(command)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "message": "Order status updated successfully",
        "order": order
    }


@app.post("/orders/{order_id}/cancel")
def cancel_order(order_id: int):
    command = CancelOrderCommand(order_id=order_id)

    handler = CancelOrderHandler(order_write_repository, event_bus)
    order = handler.handle(command)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "message": "Order cancelled successfully",
        "order": order
    }


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    query = GetOrderQuery(order_id=order_id)

    handler = GetOrderHandler(order_read_repository)
    order = handler.handle(query)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@app.get("/customers/{customer_id}/orders")
def list_orders_by_customer(customer_id: int):
    query = ListOrdersByCustomerQuery(customer_id=customer_id)

    handler = ListOrdersByCustomerHandler(order_read_repository)
    orders = handler.handle(query)

    return orders


@app.get("/broker/events")
def list_published_events():
    return event_bus.get_published_events()
