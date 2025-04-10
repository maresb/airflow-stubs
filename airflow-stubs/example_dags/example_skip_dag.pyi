from airflow.exceptions import AirflowSkipException as AirflowSkipException
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.utils.context import Context as Context
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

class EmptySkipOperator(BaseOperator):
    ui_color: str
    def execute(self, context: Context): ...

def create_test_pipeline(suffix, trigger_rule) -> None: ...
