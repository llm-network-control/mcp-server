"""
Репозиторий для работы с базой
"""
from typing import List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from routers.models import Router as RouterModel

from .adapters import db_to_router, router_to_db
from .models import Router as DbRouter


async def save_router(
    session: AsyncSession,
    router_model: RouterModel,
) -> DbRouter:
    """
    Сохраняем роутер в БД
    :param session: текущая сессия
    :param router_model: модель роутера
    :return: Объект роутера в ОРМ
    """
    db_router = router_to_db(router_model)
    session.add(db_router)
    await session.commit()
    await session.refresh(db_router)
    return db_router


async def get_routers_list(
        session: AsyncSession,
) -> List[RouterModel]:
    """
    Получаем все роутеры из базы
    :param session: текущая сессия
    :return: список моделей роутеров
    """
    query = (
        select(DbRouter).
        order_by(DbRouter.created_at)
    )
    result = await session.execute(query)
    objects = result.scalars().all()
    result_list = [
        db_to_router(item)
        for item in objects
    ]
    return result_list


async def get_router_by_ip(
        session: AsyncSession,
        ip: str,
) -> RouterModel | None:
    """
    Получение роутера по ip
    :param session: Текущая сессия
    :param ip: IP адрес
    :return: RouterModel или None
    """
    query = (
        select(DbRouter).
        where(DbRouter.ip==ip)
    )
    result = await session.execute(query)
    item = result.scalars().first()
    result = db_to_router(item) if item else None
    return result


async def get_routers_by_ssid(
    session: AsyncSession,
    ssid: str,
) -> List[RouterModel]:
    """
    Получаем роутеры по SSID
    :param session: текущая сессия
    :param ssid: имя wifi сети
    :return: список моделей роутеров
    """
    query = (
        select(DbRouter).
        where(DbRouter.ssid == ssid).
        order_by(DbRouter.created_at)
    )
    result = await session.execute(query)
    objects = result.scalars().all()
    result_list = [
        db_to_router(item)
        for item in objects
    ]
    return result_list


async def delete_routers(session: AsyncSession) -> None:
    """
    Удалить все роутеры
    :param session: текущая сессия
    :return: None
    """
    query = delete(DbRouter)
    await session.execute(query)
    await session.commit()
