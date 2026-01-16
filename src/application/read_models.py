from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class OrderView:
    """
    Read model for Order queries.

    This is a denormalized, read-only projection
    optimized for queries and presentation.
    """

    id: UUID
    customer_id: UUID
    status: str
    total_amount: float
    created_at: datetime
    updated_at: datetime
