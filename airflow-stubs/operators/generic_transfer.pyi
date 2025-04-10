from _typeshed import Incomplete
from airflow.hooks.base import BaseHook as BaseHook
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.context import Context as Context
from typing import Sequence

class GenericTransfer(BaseOperator):
    template_fields: Sequence[str]
    template_ext: Sequence[str]
    template_fields_renderers: Incomplete
    ui_color: str
    sql: Incomplete
    destination_table: Incomplete
    source_conn_id: Incomplete
    destination_conn_id: Incomplete
    preoperator: Incomplete
    insert_args: Incomplete
    def __init__(self, *, sql: str, destination_table: str, source_conn_id: str, destination_conn_id: str, preoperator: str | list[str] | None = None, insert_args: dict | None = None, **kwargs) -> None: ...
    def execute(self, context: Context): ...
