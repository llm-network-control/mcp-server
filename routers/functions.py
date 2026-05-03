"""
Основные функции управления роутерами
"""
from ipaddress import IPv4Address

from db import repository
from db.session import session_cls

from . import models

# async def parse_network(networks: set[IPv4Network]) -> int:
#     """
#     Анализ сети, поиск доступных устройств
#     :param networks: список сетей, например IPv4Network("172.14.80.0/24")
#     :return: Количество найденных устройств
#     """
#     assert networks
#     return 2


async def get_all_available_routers() -> list[models.Router]:
    """
    Получение списка доступных роутеров
    :return: список доступных роутеров из базы данных
    """
    async with session_cls() as session:
        router_list = await repository.get_routers_list(
            session,
        )
    return router_list


async def get_router_by_ip(ip: IPv4Address) -> models.Router | None:
    """
    Поиск роутера по ip адресу
    :param ip: IP адрес роутера
    :return: Router или None
    """
    async with session_cls() as session:
        router = await repository.get_router_by_ip(
            session,
            ip = str(ip)
        )
    return router


async def get_routers_by_ssid(ssid: str) -> list[models.Router]:
    """
    Поиск роутеров по имени WiFi сети
    :param ssid: имя wifi сети
    :return: Router
    """
    async with session_cls() as session:
        routers = await repository.get_routers_by_ssid(
            session,
            ssid=ssid
        )
    return routers
