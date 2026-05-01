"""
Модели данных
"""
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей
    """


class Router(Base):
    """
    Анкета пользователя в БД
    """

    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(primary_key=True)
    ip: Mapped[str] = mapped_column(String(15))  # 255.255.255.255
    firmware: Mapped[str] = mapped_column(String(100))
    ssid: Mapped[str] = mapped_column(String(32), nullable=True)  # 32 байт max
    wifi_password: Mapped[str] = mapped_column(String(100), nullable=True)
    pppoe_username: Mapped[str] = mapped_column(String(256), nullable=True)
    pppoe_password: Mapped[str] = mapped_column(String(100), nullable=True)

    created_at: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # pylint: disable=not-callable
    )
