from core.utils import env

MYSQL_HOST = env("MYSQL_HOST", "localhost")
MYSQL_PORT = env("MYSQL_PORT", "3306")
MYSQL_USER = env("MYSQL_USER", "root")
MYSQL_PASSWORD = env("MYSQL_PASSWORD", "")
MYSQL_DB = env("MYSQL_DB", "app")


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
