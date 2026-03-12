import os
from urllib.parse import urlparse

import mysql.connector


def _db_settings_from_env():
    mysql_url = os.getenv("MYSQL_URL")

    if mysql_url:
        parsed = urlparse(mysql_url)
        return {
            "host": parsed.hostname,
            "port": parsed.port or 3306,
            "user": parsed.username,
            "password": parsed.password,
            "database": (parsed.path or "").lstrip("/"),
        }

    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "998877"),
        "database": os.getenv("DB_NAME", "subhash_college"),
    }


settings = _db_settings_from_env()

db = mysql.connector.connect(
    host=settings["host"],
    port=settings["port"],
    user=settings["user"],
    password=settings["password"],
    database=settings["database"],
)

cursor = db.cursor()

print("Database Connected Successfully")