from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import uuid


class OrderStatus(Enum):
    CREATED = "CREATED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float

    def total_price(self) -> float:
        return self.quantity * self.price


@dataclass
class Order:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.CREATED
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @staticmethod
    def create(customer_id: str, items: List[OrderItem]) -> "Order":
        if not items:
            raise ValueError("Order must contain at least one item")

        return Order(
            order_id=str(uuid.uuid4()),
            customer_id=customer_id,
            items=items,
        )

    @property
    def total_amount(self) -> float:
        return sum(item.total_price() for item in self.items)

    def pay(self) -> None:
        if self.status != OrderStatus.CREATED:
            raise ValueError("Only CREATED orders can be paid")

        self.status = OrderStatus.PAID
        self.updated_at = datetime.utcnow()

    def ship(self) -> None:
        if self.status != OrderStatus.PAID:
            raise ValueError("Only PAID orders can be shipped")

        self.status = OrderStatus.SHIPPED
        self.updated_at = datetime.utcnow()

    def cancel(self) -> None:
        if self.status == OrderStatus.SHIPPED:
            raise ValueError("Shipped orders cannot be cancelled")

        self.status = OrderStatus.CANCELLED
        self.updated_at = datetime.utcnow()
