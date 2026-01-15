from typing import Optional

from src.application.ports.order_repository import OrderRepository
from src.domain.order import Order, OrderId
from src.infrastructure.persistence.models.order_model import OrderModel


class PostgresOrderRepository(OrderRepository):
    """
    PostgreSQL implementation of OrderRepository.

    This class is responsible ONLY for persistence mapping.
    Transaction boundaries are managed externally (Unit of Work).
    """

    def __init__(self, session) -> None:
        self._session = session

    def save(self, order: Order) -> None:
        model = OrderModel.from_domain(order)
        self._session.add(model)

    def get_by_id(self, order_id: OrderId) -> Optional[Order]:
        model: OrderModel | None = (
            self._session.query(OrderModel)
            .filter_by(id=order_id.value)
            .one_or_none()
        )

        if model is None:
            return None

        return model.to_domain()
