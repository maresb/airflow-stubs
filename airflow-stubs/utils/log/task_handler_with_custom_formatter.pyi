import logging
from airflow.configuration import conf as conf
from airflow.utils.helpers import parse_template_string as parse_template_string, render_template_to_string as render_template_to_string
from typing import ClassVar

TYPE_CHECKING: bool

class TaskHandlerWithCustomFormatter(logging.StreamHandler):
    prefix_jinja_template: ClassVar[None] = ...
    def set_context(self, ti) -> None: ...
