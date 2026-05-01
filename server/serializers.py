"""
Serializers
"""
from routers.models import Router


def serialize(router: Router) -> dict:
    """
    Преобразование router в dict
    :param router: Router
    :return: dict
    """
    return router.__dict__
