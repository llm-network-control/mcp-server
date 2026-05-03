"""
Entrypoint
"""
from config import SERVER_HOST, SERVER_PORT
from server import mcp

if __name__ == "__main__":
    mcp.run(transport="http", host=SERVER_HOST, port=SERVER_PORT)
