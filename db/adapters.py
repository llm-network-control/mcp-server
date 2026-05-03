"""
Соответствие Моделей и Моделей в ORM
"""
from ipaddress import IPv4Address

from routers.models import Router as RouterModel
from routers.models import create_router

from .models import Router as DbRouter


def router_to_db(router_model: RouterModel) -> DbRouter:
    """
    RouterModel -> DbRouter
    :param router_model: RouterModel
    :return: RouterModel
    """
    db_router = DbRouter(
        ip=str(router_model.ip),
        firmware=router_model.firmware,
        ssid=router_model.ssid,
        wifi_password=router_model.wifi_password,
        pppoe_username=router_model.pppoe_username,
        pppoe_password=router_model.pppoe_password,
    )
    return db_router


def db_to_router(db_router: DbRouter) -> RouterModel:
    """
    DbRouter -> RouterModel
    :param db_router: DbRouter
    :return: RouterModel
    """
    router_model = create_router(
        ip=IPv4Address(db_router.ip),
        firmware=db_router.firmware,
        ssid=db_router.ssid,
        wifi_password=db_router.wifi_password,
        pppoe_username=db_router.pppoe_username,
        pppoe_password=db_router.pppoe_password,
    )
    return router_model
