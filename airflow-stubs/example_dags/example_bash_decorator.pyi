from airflow.decorators import dag as dag, task as task
from airflow.exceptions import AirflowSkipException as AirflowSkipException
from airflow.models.baseoperator import chain as chain
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.weekday import WeekDay as WeekDay

def example_bash_decorator(): ...
