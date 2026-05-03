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
    result_dict = router.__dict__
    result_dict['ip'] = str(router.__dict__['ip'])
    return result_dict
