"""
MCP server tools
"""
from ipaddress import IPv4Address

from fastmcp import FastMCP

import routers

from .serializers import serialize

mcp = FastMCP(
    name="Network Control MCP Server",
    instructions='The server allows you to receive information about '
                 'routers on the network, as well as manage their behavior'
)


# @mcp.tool(
#     name="scan_network",
#     description=(
#         "Scan one or more IPv4 networks for available routers. "
#         "Use when the user asks to discover or scan devices."
#     )
# )
# async def scan_network(
#     networks: list[str],
# ) -> dict:
#     """
#     networks example:
#     ["172.14.80.0/24", "172.14.81.0/24"]
#     """
#
#     parsed_networks = {
#         IPv4Network(net)
#         for net in networks
#     }
#
#     count = await routers.parse_network(
#         networks=parsed_networks
#     )
#
#     return {
#         "devices_found": count,
#     }


@mcp.tool(
    name="list_routers",
    title='List routers',
    description=(
        "Return all routers currently stored in the database."
    )
)
async def list_routers() -> list[dict]:
    """
    Список всех роутеров
    """
    routers_list = await routers.get_all_available_routers()

    return [
        serialize(router)
        for router in routers_list
    ]


@mcp.tool(
    name="get_router_by_ip",
    title='Get router by ip',
    description=(
        "Get information about a router by IP address."
    )
)
async def get_router_by_ip(
    ip: str,
) -> dict:
    """
    Получение роутера по ip адресу
    :param ip: строка IP адреса
    :return: словарь с данными роутера
    """
    router = await routers.get_router_by_ip(
        ip=IPv4Address(ip)
    )

    return serialize(router)


@mcp.tool(
    name="find_routers_by_ssid",
    title='Find routers by SSID',
    description=(
        "Find routers by WiFi SSID name."
    )
)
async def find_routers_by_ssid(
    ssid: str,
) -> list[dict]:
    """
    Получение роутеров по SSID имени wifi
    :param ssid: SSID
    :return: список с данными рутеров
    """
    found = await routers.get_routers_by_ssid(
        ssid=ssid
    )

    return [
        serialize(router)
        for router in found
    ]
