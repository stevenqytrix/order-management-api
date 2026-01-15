from typing import List, Protocol

from src.domain.order import Order, OrderItem


class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        ...

    def get_by_id(self, order_id: str) -> Order:
        ...


class CreateOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, customer_id: str, items: List[OrderItem]) -> Order:
        order = Order.create(customer_id=customer_id, items=items)
        self.repository.save(order)
        return order


class PayOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: str) -> Order:
        order = self.repository.get_by_id(order_id)
        order.pay()
        self.repository.save(order)
        return order


class ShipOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: str) -> Order:
        order = self.repository.get_by_id(order_id)
        order.ship()
        self.repository.save(order)
        return order


class CancelOrderUseCase:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def execute(self, order_id: str) -> Order:
        order = self.repository.get_by_id(order_id)
        order.cancel()
        self.repository.save(order)
        return order
