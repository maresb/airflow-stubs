from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.decorators import task as task
from airflow.example_dags.libs.helper import print_stuff as print_stuff
from airflow.models.dag import DAG as DAG

log: Incomplete
worker_container_repository: Incomplete
worker_container_tag: Incomplete
start_task_executor_config: Incomplete

def task_with_template() -> None: ...
def task_with_local(ds: Incomplete | None = None, **kwargs): ...
