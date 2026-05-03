"""
Test MCP server with MCP client
"""
import pytest
import pytest_asyncio
from fastmcp import Client

from server.tools import mcp


@pytest_asyncio.fixture
async def client():
    """
    Fixture текущий тестовый mcp клиент
    """
    current_client = Client(mcp)
    async with current_client:
        await current_client.ping()
        yield current_client


@pytest.mark.asyncio
async def test_list_tools(client: Client):
    """
    Проверка списка tools
    :param client: текущий mcp клиент
    """
    tools = await client.list_tools()
    expected_tools = {
        "list_routers",
        "get_router_by_ip",
        "find_routers_by_ssid",
    }
    current_tool_names = [
        tool.name for tool in tools
    ]
    assert expected_tools == set(current_tool_names)
