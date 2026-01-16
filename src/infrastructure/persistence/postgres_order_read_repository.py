from typing import Optional

from sqlalchemy import text

from domain.order import OrderId
from application.ports.order_read_repository import OrderReadRepository
from application.read_models import OrderView


class PostgresOrderReadRepository(OrderReadRepository):
    """
    PostgreSQL implementation of OrderReadRepository.

    Optimized for read-only queries.
    Returns denormalized OrderView projections.
    """

    def __init__(self, session):
        self._session = session

    def get_by_id(self, order_id: OrderId) -> Optional[OrderView]:
        query = text("""
            SELECT
                id,
                customer_id,
                status,
                total_amount,
                created_at,
                updated_at
            FROM orders
            WHERE id = :order_id
        """)

        row = self._session.execute(
            query,
            {"order_id": order_id.value}
        ).mappings().one_or_none()

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
