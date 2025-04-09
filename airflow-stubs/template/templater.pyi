import jinja2
from airflow import DAG as DAG
from airflow.io.path import ObjectStoragePath as ObjectStoragePath
from airflow.models.operator import Operator as Operator
from airflow.utils.context import Context as Context
from airflow.utils.helpers import render_template_as_native as render_template_as_native, render_template_to_string as render_template_to_string
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.mixins import ResolveMixin as ResolveMixin
from dataclasses import dataclass
from typing import Any, Collection, Iterable, Sequence

@dataclass(frozen=True)
class LiteralValue(ResolveMixin):
    value: Any
    def iter_references(self) -> Iterable[tuple[Operator, str]]: ...
    def resolve(self, context: Context, *, include_xcom: bool = True) -> Any: ...

class Templater(LoggingMixin):
    template_fields: Collection[str]
    template_ext: Sequence[str]
    def get_template_env(self, dag: DAG | None = None) -> jinja2.Environment: ...
    def prepare_template(self) -> None: ...
    def resolve_template_files(self) -> None: ...
    def render_template(self, content: Any, context: Context, jinja_env: jinja2.Environment | None = None, seen_oids: set[int] | None = None) -> Any: ...
