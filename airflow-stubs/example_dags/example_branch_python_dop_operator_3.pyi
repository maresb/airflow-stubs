from airflow.decorators import task as task
from airflow.decorators.base import should_run as should_run
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import cond as cond
from airflow.operators.empty import EmptyOperator as EmptyOperator, empty_task_1 as empty_task_1, empty_task_2 as empty_task_2
