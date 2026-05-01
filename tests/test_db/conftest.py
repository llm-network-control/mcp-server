"""
Fixtures для тестирования базы данных
"""
import pytest_asyncio
import pytest
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Router as DbRouter
from db import adapters
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


async def clear_db(current_session: AsyncSession):
    query = delete(DbRouter)
    await current_session.execute(query)
    await current_session.commit()


@pytest_asyncio.fixture
async def session():
    async with session_cls() as current_session:
        yield current_session
        await clear_db(current_session)
