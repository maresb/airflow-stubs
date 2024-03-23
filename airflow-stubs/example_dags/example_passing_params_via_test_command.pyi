from airflow.decorators import task as task
from airflow.decorators.base import my_py_command as my_py_command, print_env_vars as print_env_vars
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import env_var_test_task as env_var_test_task, run_this as run_this
from airflow.operators.bash import BashOperator as BashOperator, also_run_this as also_run_this

my_command: str
