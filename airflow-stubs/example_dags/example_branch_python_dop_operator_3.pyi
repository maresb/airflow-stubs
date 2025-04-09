from _typeshed import Incomplete
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator

def should_run(**kwargs) -> str: ...

cond: Incomplete
empty_task_1: Incomplete
empty_task_2: Incomplete
