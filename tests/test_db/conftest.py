"""
Fixtures для тестирования базы данных
"""
import pytest
from db.models import Router as DbRouter
from db import adapters


@pytest.fixture
def one_db_router(one_router) -> DbRouter:
    """
    Роутер в ОРМ
    :param one_router: Модель роутера
    :return: DbRouter
    """
    db_router = adapters.router_to_db(one_router)
    return db_router
