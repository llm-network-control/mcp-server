"""
Test routers/models
"""
from routers import models


def test_create_router(one_router_data_dict: dict, one_router: models.Router):
    """
    Test: create_router: positive
    """
    assert one_router.ip == one_router_data_dict['ip']
    assert one_router.firmware == one_router_data_dict['firmware']
    assert one_router.ssid == one_router_data_dict['ssid']
    assert one_router.wifi_password == one_router_data_dict['wifi_password']
    assert one_router.pppoe_username == one_router_data_dict['pppoe_username']
    assert one_router.pppoe_password == one_router_data_dict['pppoe_password']
