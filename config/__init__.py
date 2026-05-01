from os import getenv

DATABASE_URL = getenv('DATABASE_URL', 'sqlite+aiosqlite:///./db.sqlite3')
SYNC_DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///./db.sqlite3')
