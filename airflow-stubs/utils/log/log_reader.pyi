from airflow.configuration import conf as conf
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.helpers import render_log_filename as render_log_filename
from airflow.utils.log.logging_mixin import ExternalLoggingMixin as ExternalLoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from functools import cached_property as cached_property
from sqlalchemy.orm.session import Session as Session
from typing import Iterator

class TaskLogReader:
    STREAM_LOOP_SLEEP_SECONDS: int
    def read_log_chunks(self, ti: TaskInstance, try_number: int | None, metadata) -> tuple[list[tuple[tuple[str, str]]], dict[str, str]]: ...
    def read_log_stream(self, ti: TaskInstance, try_number: int | None, metadata: dict) -> Iterator[str]: ...
    @cached_property
    def log_handler(self): ...
    @property
    def supports_read(self): ...
    @property
    def supports_external_link(self) -> bool: ...
    def render_log_filename(self, ti: TaskInstance, try_number: int | None = None, *, session: Session = ...) -> str: ...
