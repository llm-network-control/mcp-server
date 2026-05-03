"""
Test server/serializers
"""
from routers import models
from server import serializers


def test_serialize(one_router_data_dict: dict, one_router: models.Router):
    """
    Test serialize: positive
    """
    expected_dict = one_router_data_dict
    expected_dict['ip'] = str(one_router_data_dict['ip'])
    assert serializers.serialize(one_router) == expected_dict
