from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from src.domain.order import Order, OrderStatus


@dataclass
class OrderModel:
    id: UUID
    customer_id: UUID
    status: str
    total_amount: int

    @classmethod
    def from_domain(cls, order: Order) -> "OrderModel":
        return cls(
            id=order.id,
            customer_id=order.customer_id,
            status=order.status.value,
            total_amount=order.total_amount,
        )

    def to_domain(self) -> Order:
        return Order(
            id=self.id,
            customer_id=self.customer_id,
            status=OrderStatus(self.status),
            total_amount=self.total_amount,
        )

