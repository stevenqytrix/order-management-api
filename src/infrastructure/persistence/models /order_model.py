from dataclasses import dataclass
from uuid import UUID

from src.domain.order import (
    Order,
    OrderId,
    CustomerId,
    OrderStatus,
)


@dataclass(frozen=True)
class OrderModel:
    """
    Persistence representation of Order aggregate.

    This model is a pure data container and must not
    contain domain logic.
    """

    id: UUID
    customer_id: UUID
    status: str
    total_amount: float

    @classmethod
    def from_domain(cls, order: Order) -> "OrderModel":
        """
        Convert a domain Order aggregate into its persistence form.
        """
        return cls(
            id=order.id.value,
            customer_id=order.customer_id.value,
            status=order.status.value,
            total_amount=order.total_amount,
        )

    def to_domain(self) -> Order:
        """
        Rehydrate a domain Order aggregate from persistence state.

        NOTE:
        This must bypass invariants already validated at creation time.
        """
        return Order.rehydrate(
            id=OrderId(self.id),
            customer_id=CustomerId(self.customer_id),
            status=OrderStatus(self.status),
            total_amount=self.total_amount,
        )

