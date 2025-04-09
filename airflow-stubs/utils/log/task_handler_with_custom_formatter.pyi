import logging
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.helpers import parse_template_string as parse_template_string, render_template_to_string as render_template_to_string
from jinja2 import Template as Template

logger: Incomplete

class TaskHandlerWithCustomFormatter(logging.StreamHandler):
    prefix_jinja_template: Template | None
    def set_context(self, ti) -> None: ...
