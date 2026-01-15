from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Sequence
from uuid import UUID, uuid4


# =========
# Domain Errors
# =========

class DomainError(Exception):
    pass


class InvalidOrderState(DomainError):
    pass


# =========
# Value Objects
# =========

@dataclass(frozen=True)
class OrderId:
    value: UUID

    @staticmethod
    def new() -> "OrderId":
        return OrderId(uuid4())


@dataclass(frozen=True)
class CustomerId:
    value: str


# =========
# Domain Model
# =========

class OrderStatus(Enum):
    CREATED = "CREATED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


@dataclass(frozen=True)
class OrderItem:
    product_id: str
    quantity: int
    price: float

    def total_price(self) -> float:
        return self.quantity * self.price


@dataclass
class Order:
    id: OrderId
    customer_id: CustomerId
    items: Sequence[OrderItem]
    status: OrderStatus = OrderStatus.CREATED
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @staticmethod
    def create(*, customer_id: CustomerId, items: Sequence[OrderItem]) -> "Order":
        if not items:
            raise DomainError("Order must contain at least one item")

        return Order(
            id=OrderId.new(),
            customer_id=customer_id,
            items=items,
        )

    @property
    def total_amount(self) -> float:
        return sum(item.total_price() for item in self.items)

    def pay(self) -> None:
        if self.status is not OrderStatus.CREATED:
            raise InvalidOrderState("Only CREATED orders can be paid")

        self.status = OrderStatus.PAID
        self.updated_at = datetime.utcnow()

    def ship(self) -> None:
        if self.status is not OrderStatus.PAID:
            raise InvalidOrderState("Only PAID orders can be shipped")

        self.status = OrderStatus.SHIPPED
        self.updated_at = datetime.utcnow()

    def cancel(self) -> None:
        if self.status is OrderStatus.SHIPPED:
            raise InvalidOrderState("Shipped orders cannot be cancelled")

        self.status = OrderStatus.CANCELLED
        self.updated_at = datetime.utcnow()
