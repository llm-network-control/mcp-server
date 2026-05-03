"""
Генерация случайных данных для тестирования MCP сервера
"""
import asyncio
import random
from ipaddress import IPv4Address

from faker import Faker
from faker.providers import internet
from faker_wifi_essid import WifiESSID

from db.repository import delete_routers, save_router
from db.session import session_cls
from routers.models import Router as RouterModel
from routers.models import create_router

fake = Faker()
fake.add_provider(internet)
fake.add_provider(WifiESSID)


def random_version():
    """
    Случайная версия прошивки
    """
    major = {random.randint(1,10)}
    minor = {random.randint(1,10)}
    return f'v{major}.{minor}'


def random_router_model() -> RouterModel:
    """
    Создание случайного роутера
    :return: Модель роутера
    """
    ip: IPv4Address = IPv4Address(fake.ipv4_private())
    firmware: str = f'Fake Firmware {random_version()}'
    ssid: str = fake.wifi_essid()
    wifi_password: str = fake.password()
    pppoe_username: str = fake.user_name()
    pppoe_password: str = fake.password()

    return create_router(
        ip,
        firmware,
        ssid,
        wifi_password,
        pppoe_username,
        pppoe_password,
    )


def generate_data(count: int = 100) -> list[RouterModel]:
    """
    Генерация данных
    :param count:
    :return:
    """
    return [
        random_router_model()
        for _ in range(count)
    ]


async def save_data(router_models: list[RouterModel]) -> int:
    """
    Сохранение данных в базу данных
    :param router_models: список моделей роутеров
    :return: кол-во записей
    """

    async with session_cls() as session:
        await delete_routers(session)
        for router_model in router_models:
            await save_router(session, router_model)
    return len(router_models)


async def main():
    """
    Функция запуска
    """
    print('Генерирую случайные данные...')
    router_models = generate_data(100)
    print('Данные созданы')
    print('Сохраняю данные в базу...')
    count = await save_data(router_models)
    print(f'{count} записей было загружено')

if __name__ == '__main__':
    asyncio.run(main())
