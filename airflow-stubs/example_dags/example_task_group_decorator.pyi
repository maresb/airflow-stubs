from airflow.decorators import task as task
from airflow.decorators.base import task_1 as task_1, task_2 as task_2, task_3 as task_3, task_end as task_end, task_start as task_start
from airflow.decorators.task_group import task_group as task_group, task_group_function as task_group_function
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import end_task as end_task, start_task as start_task
from airflow.utils.task_group import current_task_group as current_task_group

i: int
