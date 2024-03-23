from airflow.configuration import conf as conf
from airflow.decorators import task as task
from airflow.decorators.base import task_with_local as task_with_local, task_with_template as task_with_template
from airflow.example_dags.libs.helper import print_stuff as print_stuff
from airflow.models.dag import DAG as DAG, dag as dag

worker_container_repository: str
worker_container_tag: str
start_task_executor_config: dict
