from airflow.configuration import conf as conf
from sqlalchemy.sql.sqltypes import String

SQL_ALCHEMY_SCHEMA: str
naming_convention: dict
ID_LEN: int
def get_id_collation_args(): ...

COLLATION_ARGS: dict
def StringID(**kwargs) -> String: ...
