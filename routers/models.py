"""
Модели данных
"""
from ipaddress import IPv4Address
import dataclasses


@dataclasses.dataclass(frozen=True)
class Router:
    """
    Данные роутера
    """
    ip: IPv4Address
    firmware: str
    ssid: str = None
    wifi_password: str = None
    pppoe_username: str = None
    pppoe_password: str = None


def create_router(
        ip: IPv4Address,
        firmware: str,
        ssid: str = None,
        wifi_password: str = None,
        pppoe_username: str = None,
        pppoe_password: str = None,
) -> Router:
    """
    Создание роутера
    :param ip: IP адрес
    :param firmware: Прошивка
    :param ssid: Имя wifi
    :param wifi_password: Пароль wifi
    :param pppoe_username: Имя пользователя сетевого подключения
    :param pppoe_password: Пароль от сетевого подключения

    :return: Router
    """
    return Router(
        ip=ip,
        firmware=firmware,
        ssid=ssid,
        wifi_password=wifi_password,
        pppoe_username=pppoe_username,
        pppoe_password=pppoe_password,
    )
