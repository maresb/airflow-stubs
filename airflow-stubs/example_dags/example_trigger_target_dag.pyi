from airflow.decorators import task as task
from airflow.decorators.base import run_this_func as run_this_func
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import run_this as run_this
from airflow.operators.bash import BashOperator as BashOperator, bash_task as bash_task
