from abc import ABC, abstractmethod
from typing import Optional

from domain.order import Order, OrderId


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        ...

    @abstractmethod
    def get_by_id(self, order_id: OrderId) -> Optional[Order]:
        ...
