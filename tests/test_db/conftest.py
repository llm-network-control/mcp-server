"""
Fixtures для тестирования базы данных
"""
import pytest
import pytest_asyncio

from db import adapters
from db.models import Router as DbRouter
from db.repository import delete_routers
from db.session import session_cls


@pytest.fixture
def one_db_router(one_router) -> DbRouter:
    """
    Роутер в ОРМ
    :param one_router: Модель роутера
    :return: DbRouter
    """
    db_router = adapters.router_to_db(one_router)
    return db_router


@pytest_asyncio.fixture
async def session():
    """
    Fixture для текущей сессии
    :return: Текущая сессия
    """
    async with session_cls() as current_session:
        yield current_session
        await delete_routers(current_session)
