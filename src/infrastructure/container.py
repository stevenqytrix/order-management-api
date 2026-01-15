from application.use_cases import (
    CreateOrderUseCase,
    PayOrderUseCase,
    ShipOrderUseCase,
    CancelOrderUseCase,
    GetOrderUseCase,
)
from infrastructure.persistence.postgres_order_repository import PostgresOrderRepository


def build_order_repository():
    # placeholder: connection/session verrà iniettata dopo
    return PostgresOrderRepository()


def build_create_order_use_case():
    return CreateOrderUseCase(build_order_repository())


def build_pay_order_use_case():
    return PayOrderUseCase(build_order_repository())


def build_ship_order_use_case():
    return ShipOrderUseCase(build_order_repository())


def build_cancel_order_use_case():
    return CancelOrderUseCase(build_order_repository())


def build_get_order_use_case():
    return GetOrderUseCase(build_order_repository())
