from _typeshed import Incomplete
from airflow.decorators import dag as dag, task as task

def sla_callback(dag, task_list, blocking_task_list, slas, blocking_tis) -> None: ...
def example_sla_dag() -> None: ...

example_dag: Incomplete
