from abc import ABC, abstractmethod
from typing import Optional

from domain.order import OrderId
from application.read_models import OrderView


class OrderReadRepository(ABC):
    """
    Read-only contract for querying Orders.

    This port is optimized for reads and MUST NOT:
    - modify state
    - enforce domain invariants
    - expose domain aggregates
    """

    @abstractmethod
    def get_by_id(self, order_id: OrderId) -> Optional[OrderView]:
        """
        Retrieve a read-only view of an Order.

        Returns None if the Order does not exist.
        """
        ...
