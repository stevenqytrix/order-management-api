from typing import Optional
from uuid import UUID

from src.application.ports.order_repository import OrderRepository
from src.domain.order import Order
from src.infrastructure.persistence.models.order_model import OrderModel


class PostgresOrderRepository(OrderRepository):
    def __init__(self, session):
        self._session = session

    def save(self, order: Order) -> None:
        model = OrderModel.from_domain(order)
        self._session.add(model)
        self._session.commit()

    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        model: OrderModel | None = (
            self._session.query(OrderModel)
            .filter_by(id=order_id)
            .one_or_none()
        )

        if model is None:
            return None

        return model.to_domain()
