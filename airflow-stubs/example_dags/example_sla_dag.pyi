from airflow.decorators import task as task
from airflow.models.dag import dag as dag, example_dag as example_dag

def sla_callback(dag, task_list, blocking_task_list, slas, blocking_tis): ...
def example_sla_dag(*args, **kwargs): ...