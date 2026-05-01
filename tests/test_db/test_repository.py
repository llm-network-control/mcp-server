"""
Test db/repository
"""
import pytest
from routers.models import Router as RouterModel
from db import repository


@pytest.mark.asyncio
async def test_get_routers_list_empty(session):
    """
    Test get_routers_list: positive: empty DB
    """
    result = await repository.get_routers_list(session)
    assert result == []


@pytest.mark.asyncio
async def test_save_router(session, one_router: RouterModel):
    """
    Test save_router: positive
    :param session: Текущая сессия
    :param one_router: Модель роутера
    """
    # В базе нет данных
    result = await repository.get_routers_list(session)
    assert result == []
    # Создаем роутер
    await repository.save_router(session, one_router)
    # В базе 1 роутер
    result = await repository.get_routers_list(session)
    assert result == [one_router]


@pytest.mark.asyncio
async def test_get_router_by_ip(session, one_router: RouterModel):
    """
    Test get_router_by_ip: positive
    :param session: Текущая сессия
    :param one_router: Модель роутера
    """
    # Роутера нет
    result = await repository.get_router_by_ip(session, str(one_router.ip))
    assert result is None
    # Создаем роутер
    await repository.save_router(session, one_router)
    # Ищем его
    result = await repository.get_router_by_ip(session, str(one_router.ip))
    assert result == one_router


@pytest.mark.asyncio
async def test_get_routers_by_ssid(session, one_router: RouterModel):
    """
    Test get_routers_by_ssid: positive
    :param session: Текущая сессия
    :param one_router: Модель роутера
    """
    # Роутеров нет
    result = await repository.get_routers_by_ssid(session, str(one_router.ssid))
    assert result == []
    # Создаем роутер
    await repository.save_router(session, one_router)
    # Ищем его
    result = await repository.get_routers_by_ssid(session, str(one_router.ssid))
    assert result == [one_router]
