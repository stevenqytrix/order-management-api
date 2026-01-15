from abc import ABC, abstractmethod
from typing import Optional

from domain.order import Order, OrderId


class OrderRepository(ABC):
    """
    Contract for persisting and retrieving Order aggregates.

    Guarantees:
    - Works only with fully valid Order aggregates
    - Persistence is atomic (no partial updates)
    - save() is idempotent for the same OrderId
    - No infrastructure or framework concepts leak here
    """

    @abstractmethod
    def save(self, order: Order) -> None:
        """
        Persist the given Order aggregate.

        Implementations must ensure atomic write.
        """
        ...

    @abstractmethod
    def get_by_id(self, order_id: OrderId) -> Optional[Order]:
        """
        Retrieve an Order aggregate by its identity.

        Returns None if the Order does not exist.
        """
        ...

