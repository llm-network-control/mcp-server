"""
Config package
"""
from os import getenv

DB_PATH = getenv('DB_PATH', './db.sqlite3')

DATABASE_URL = f'sqlite+aiosqlite:///{DB_PATH}'
SYNC_DATABASE_URL = f'sqlite:///{DB_PATH}'
