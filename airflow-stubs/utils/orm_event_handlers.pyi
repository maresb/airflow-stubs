from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.utils.sqlalchemy import get_orm_mapper as get_orm_mapper

log: Incomplete

def setup_event_handlers(engine) -> None: ...
