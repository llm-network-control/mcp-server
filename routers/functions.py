"""
Основные функции управления роутерами
"""
from ipaddress import IPv4Network, IPv4Address
from . import models


async def parse_network(networks: set[IPv4Network]) -> int:
    """
    Анализ сети, поиск доступных устройств
    :param networks: список сетей, например IPv4Network("172.14.80.0/24")
    :return: Количество найденных устройств
    """
    assert networks
    return 2


async def get_all_available_routers() -> list[models.Router]:
    """
    Получение списка доступных роутеров
    :return: список доступных роутеров из базы данных
    """
    mock_data = [
        {
            'ip': IPv4Address('192.168.1.1'),
            'firmware': 'TestFirmware v1',
        },
        {
            'ip': IPv4Address('192.168.1.2'),
            'firmware': 'TestFirmware v2',
        },
    ]
    return [models.create_router(**data) for data in mock_data]


async def get_router_by_ip(ip: IPv4Address) -> models.Router:
    """
    Поиск роутера по ip адресу
    :param ip: IP адрес роутера
    :return: Router
    """
    return models.create_router(ip, firmware='Test Firmware v1')


async def get_routers_by_ssid(ssid: str) -> list[models.Router]:
    """
    Поиск роутеров по имени WiFi сети
    :param ssid: имя wifi сети
    :return: Router
    """
    return [
        models.create_router(
            ip=IPv4Address('192.168.1.1'),
            firmware='Test Firmware v1',
            ssid=ssid,
        )
    ]
