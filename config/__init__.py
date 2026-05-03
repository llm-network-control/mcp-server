"""
Config package
"""
from os import getenv

SERVER_HOST = getenv('SERVER_HOST', '127.0.0.1')
SERVER_PORT = int(getenv('SERVER_PORT', '9000'))

DB_PATH = getenv('DB_PATH', './data/db.sqlite3')

DATABASE_URL = f'sqlite+aiosqlite:///{DB_PATH}'
SYNC_DATABASE_URL = f'sqlite:///{DB_PATH}'
