"""
Test routers/functions
"""
import pytest
import pytest_asyncio

from db import repository
from db.session import session_cls
from routers import functions


@pytest_asyncio.fixture(autouse=True)
async def fill_db(one_router):
    """
    Заполняем базу тестовыми данными
    :param one_router: Модель роутера
    """
    async with session_cls() as session:
        # Чистим всё
        await repository.delete_routers(session)
        # Добавляем роутер
        await repository.save_router(session, one_router)
        yield
        # Чистим за собой
        await repository.delete_routers(session)


@pytest.mark.asyncio
async def test_get_all_available_routers(one_router):
    """
    Test get_all_available_routers: positive
    """
    result = await functions.get_all_available_routers()
    assert result == [one_router]


@pytest.mark.asyncio
async def test_get_router_by_ip(one_router):
    """
    Test get_router_by_ip: positive
    :param one_router: Модель роутера
    """
    router = await functions.get_router_by_ip(one_router.ip)
    assert router == one_router


@pytest.mark.asyncio
async def test_get_routers_by_ssid(one_router):
    """
    Test get_routers_by_ssid: positive
    :param one_router: Модель роутера
    """
    routers = await functions.get_routers_by_ssid(one_router.ssid)
    assert [one_router] == routers
