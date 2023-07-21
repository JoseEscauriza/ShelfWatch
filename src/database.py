import psycopg as pg
import environ
from src.util import ROOT_DIR

env = environ.Env()

env.read_env(str(ROOT_DIR / ".env"))


class Database():
    _instance = None

    def __new__(cls):
        if Database._instance is None:
            Database._instance = super().__new__(cls)
            Database._instance.__init__()

        return Database._instance._conn

    def __init__(self):
        self._conn = pg.connect(
            host=env.str('db_host'),
            dbname=env.str('db_name'),
            user=env.str('db_user'),
            password=env.str('db_password'),
            port=env.int('db_port')
        )
