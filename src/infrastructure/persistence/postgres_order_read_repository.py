from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from application.ports.order_read_repository import OrderReadRepository
from application.read_models import OrderView
from domain.order import OrderId
from infrastructure.persistence.models.order_model import OrderModel


class PostgresOrderReadRepository(OrderReadRepository):
    """
    PostgreSQL read-side repository.

    Implements the read-only contract using optimized queries
    and projections mapped directly to OrderView.
    """

    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, order_id: OrderId) -> Optional[OrderView]:
        stmt = (
            select(
                OrderModel.id.label("id"),
                OrderModel.customer_id.label("customer_id"),
                OrderModel.status.label("status"),
                OrderModel.total_amount.label("total_amount"),
                OrderModel.created_at.label("created_at"),
                OrderModel.updated_at.label("updated_at"),
            )
            .where(OrderModel.id == order_id.value)
        )

        row = self._session.execute(stmt).mappings().one_or_none()

        if row is None:
            return None

        return OrderView(
            id=row["id"],
            customer_id=row["customer_id"],
            status=row["status"],
            total_amount=row["total_amount"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

