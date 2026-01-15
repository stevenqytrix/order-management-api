from typing import Sequence

from domain.order import Order, OrderItem, OrderId
from application.ports.order_repository import OrderRepository
from application.errors import OrderNotFound


class _BaseOrderUseCase:
    """
    Base class for Order-related use cases.

    Centralizes application-level policies:
    - Order must exist
    - Not-found handling is consistent
    """

    def __init__(self, repository: OrderRepository):
        self._repository = repository

    def _get_order_or_fail(self, order_id: OrderId) -> Order:
        order = self._repository.get_by_id(order_id)
        if order is None:
            raise OrderNotFound(order_id)
        return order


class CreateOrder(_BaseOrderUseCase):
    """Creates a new Order aggregate."""

    def __call__(self, *, customer_id: str, items: Sequence[OrderItem]) -> Order:
        order = Order.create(customer_id=customer_id, items=items)
        self._repository.save(order)
        return order


class PayOrder(_BaseOrderUseCase):
    """Marks an existing Order as paid."""

    def __call__(self, *, order_id: OrderId) -> Order:
        order = self._get_order_or_fail(order_id)
        order.pay()
        self._repository.save(order)
        return order


class ShipOrder(_BaseOrderUseCase):
    """Ships an already paid Order."""

    def __call__(self, *, order_id: OrderId) -> Order:
        order = self._get_order_or_fail(order_id)
        order.ship()
        self._repository.save(order)
        return order


class CancelOrder(_BaseOrderUseCase):
    """Cancels an Order if cancellation is allowed."""

    def __call__(self, *, order_id: OrderId) -> Order:
        order = self._get_order_or_fail(order_id)
        order.cancel()
        self._repository.save(order)
        return order

