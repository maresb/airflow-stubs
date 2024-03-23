from airflow.decorators import task as task
from airflow.decorators.base import generate_value as generate_value, print_value as print_value
from airflow.models.dag import DAG as DAG, dag as dag, dag2 as dag2
from airflow.models.xcom_arg import xcom_args_a as xcom_args_a, xcom_args_b as xcom_args_b
from airflow.operators.bash import BashOperator as BashOperator, bash_op1 as bash_op1, bash_op2 as bash_op2
