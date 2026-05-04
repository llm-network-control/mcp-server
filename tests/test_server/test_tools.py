"""
Test server/tools
"""
import json

import pytest
import pytest_asyncio

from db import repository
from db.session import session_cls
from routers.models import Router
from server import tools
from server.serializers import serialize


@pytest_asyncio.fixture(autouse=True)
async def fill_db(one_router: Router):
    """
    Заполняем базу данных тестовыми данными
    :param one_router: модель роутера
    :return:
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
async def test_list_routers(one_router):
    """
    Test list_routers: positive
    """
    result = await tools.list_routers()
    assert [serialize(one_router)] == result


@pytest.mark.asyncio
async def test_get_router_by_ip(one_router):
    """
    Test get_router_by_ip: positive
    :param one_router: router model
    """
    result = await tools.get_router_by_ip(str(one_router.ip))
    assert serialize(one_router) == result


@pytest.mark.asyncio
async def test_find_routers_by_ssid(one_router):
    """
    Test find_router_by_ssid: positive
    :param one_router: модель роутера
    """
    result = await tools.find_routers_by_ssid(one_router.ssid)
    assert [serialize(one_router)] == result


@pytest.mark.asyncio
async def test_health_check():
    """
    Test health_check: positive
    """
    result = await tools.health_check(None)
    result_dict = json.loads(result.body.decode(encoding='utf-8'))
    assert result_dict == {"status": "healthy", "service": "mcp-server"}
