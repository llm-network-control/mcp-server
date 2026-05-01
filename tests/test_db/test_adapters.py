"""
Test db/adapters
"""
from ipaddress import IPv4Address
from db import adapters
from db.models import Router as DbRouter
from routers.models import Router as RouterModel


def test_router_to_db(one_db_router: DbRouter, one_router: RouterModel):
    """
    Test router_to_db: positive
    :param one_db_router: DbRouter
    """
    assert IPv4Address(one_db_router.ip) == one_router.ip
    assert one_db_router.firmware == one_router.firmware
    assert one_db_router.ssid == one_router.ssid
    assert one_db_router.wifi_password == one_router.wifi_password
    assert one_db_router.pppoe_username == one_router.pppoe_username
    assert one_db_router.pppoe_password == one_router.pppoe_password


def test_db_to_router(one_db_router: DbRouter, one_router: RouterModel):
    """
    Test db_to_router: positive
    :param one_db_router: DbRouter
    :param one_router: expected RouterModel data
    """
    model_router = adapters.db_to_router(one_db_router)
    assert model_router == one_router
