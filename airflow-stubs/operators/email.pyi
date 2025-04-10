from _typeshed import Incomplete
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.utils.context import Context as Context
from airflow.utils.email import send_email as send_email
from typing import Any, Sequence

class EmailOperator(BaseOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    template_ext: Sequence[str]
    ui_color: str
    to: Incomplete
    subject: Incomplete
    html_content: Incomplete
    files: Incomplete
    cc: Incomplete
    bcc: Incomplete
    mime_subtype: Incomplete
    mime_charset: Incomplete
    conn_id: Incomplete
    custom_headers: Incomplete
    def __init__(self, *, to: list[str] | str, subject: str, html_content: str, files: list | None = None, cc: list[str] | str | None = None, bcc: list[str] | str | None = None, mime_subtype: str = 'mixed', mime_charset: str = 'utf-8', conn_id: str | None = None, custom_headers: dict[str, Any] | None = None, **kwargs) -> None: ...
    def execute(self, context: Context): ...
