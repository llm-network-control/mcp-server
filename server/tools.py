"""
MCP server tools
"""
from ipaddress import IPv4Address

from fastmcp import FastMCP
from starlette.responses import JSONResponse

import routers

from .serializers import serialize

mcp = FastMCP(
    name="Network Control MCP Server",
    instructions='The server allows you to receive information about '
                 'routers on the network, as well as manage their behavior'
)


@mcp.custom_route("/health", methods=["GET"])
async def health_check(_) -> JSONResponse:
    """
    Health check
    :return: JSONResponse
    """
    return JSONResponse({"status": "healthy", "service": "mcp-server"})


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
