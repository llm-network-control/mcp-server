"""
Общие fixtures
"""
from ipaddress import IPv4Address
import pytest
from routers import models


@pytest.fixture
def one_router_data_dict() -> dict:
    """
    Тестовые данные одного роутера
    :return: dict
    """
    return {
        'ip': IPv4Address('192.168.1.1'),
        'firmware': 'Test Firmware v1',
        'ssid': 'Test WiFi Network',
        'wifi_password': 'TestNetworkPass',
        'pppoe_username': 'TestUser1',
        'pppoe_password': 'PPPoePass'
    }


@pytest.fixture
def one_router(one_router_data_dict: dict) -> models.Router:
    """
    Один роутер
    :param one_router_data_dict: Тестовые данные одного роутера (fixture)
    :return: Router
    """
    router = models.create_router(**one_router_data_dict)
    return router