from contextlib import AbstractContextManager
from typing import Callable

from application.use_cases import (
    CreateOrder,
    PayOrder,
    ShipOrder,
    CancelOrder,
)
from application.ports.order_repository import OrderRepository
from infrastructure.persistence.postgres_order_repository import PostgresOrderRepository


# =========
# Unit of Work
# =========

class UnitOfWork(AbstractContextManager):
    """
    Unit of Work implementation.

    Responsibilities:
    - Open / close persistence session
    - Control transaction boundaries
    - Expose repositories
    """

    def __init__(self, session_factory: Callable):
        self._session_factory = session_factory
        self.session = None
        self.orders: OrderRepository | None = None

    def __enter__(self):
        self.session = self._session_factory()
        self.orders = PostgresOrderRepository(self.session)
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()


# =========
# Composition Root
# =========

class Container:
    """
    Application composition root.

    - Wires dependencies
    - Defines transaction boundaries
    - Keeps infrastructure isolated
    """

    def __init__(self, *, session_factory: Callable):
        self._session_factory = session_factory

    def _uow(self) -> UnitOfWork:
        return UnitOfWork(self._session_factory)

    def create_order(self) -> CreateOrder:
        return CreateOrder(self._uow())

    def pay_order(self) -> PayOrder:
        return PayOrder(self._uow())

    def ship_order(self) -> ShipOrder:
        return ShipOrder(self._uow())

    def cancel_order(self) -> CancelOrder:
        return CancelOrder(self._uow())
