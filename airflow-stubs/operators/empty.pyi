from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.utils.context import Context as Context

class EmptyOperator(BaseOperator):
    ui_color: str
    inherits_from_empty_operator: bool
    def execute(self, context: Context): ...
