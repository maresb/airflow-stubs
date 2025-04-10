import abc
import jinja2
from abc import abstractmethod
from airflow import DAG as DAG
from airflow.template.templater import Templater as Templater
from airflow.utils.context import Context as Context, context_merge as context_merge
from typing import Sequence

class BaseNotifier(Templater, metaclass=abc.ABCMeta):
    template_fields: Sequence[str]
    template_ext: Sequence[str]
    def __init__(self) -> None: ...
    def render_template_fields(self, context: Context, jinja_env: jinja2.Environment | None = None) -> None: ...
    @abstractmethod
    def notify(self, context: Context) -> None: ...
    def __call__(self, *args) -> None: ...
