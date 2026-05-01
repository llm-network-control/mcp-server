"""
Test server/serializers
"""
from server import serializers
from routers import models


def test_serialize(one_router_data_dict: dict, one_router: models.Router):
    """
    Test serialize: positive
    """
    assert serializers.serialize(one_router) == one_router_data_dict
