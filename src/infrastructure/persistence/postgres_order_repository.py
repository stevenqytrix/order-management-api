from typing import Optional

from application.ports.order_repository import OrderRepository
from domain.order import Order


class PostgresOrderRepository(OrderRepository):
    """
    PostgreSQL implementation of the OrderRepository.
    Responsible only for persistence concerns.
    """

    def __init__(self, connection):
        """
        connection: DB connection or session (psycopg / SQLAlchemy / asyncpg)
        """
        self._connection = connection

    def save(self, order: Order) -> None:
        query = """
        INSERT INTO orders (id, customer_id, status, total_amount, created_at)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id)
        DO UPDATE SET
            status = EXCLUDED.status,
            total_amount = EXCLUDED.total_amount
        """
        self._connection.execute(
            query,
            (
                order.id,
                order.customer_id,
                order.status.value,
                order.total_amount,
                order.created_at,
            ),
        )

    def get_by_id(self, order_id: str) -> Optional[Order]:
        query = "SELECT * FROM orders WHERE id = %s"
        row = self._connection.fetch_one(query, (order_id,))

        if row is None:
            return None

        return Order(
            id=row["id"],
            customer_id=row["customer_id"],
            status=row["status"],
            total_amount=row["total_amount"],
            created_at=row["created_at"],
        )
