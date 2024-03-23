from airflow.decorators import task as task
from airflow.decorators.base import my_first_task as my_first_task, my_second_task as my_second_task, my_third_task as my_third_task, outer_setup as outer_setup, outer_teardown as outer_teardown, outer_work as outer_work
from airflow.decorators.setup_teardown import setup as setup, teardown as teardown
from airflow.decorators.task_group import section_1 as section_1, task_group as task_group
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import task_1 as task_1, task_2 as task_2, task_3 as task_3
