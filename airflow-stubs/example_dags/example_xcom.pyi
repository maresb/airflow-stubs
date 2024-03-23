from airflow.decorators import task as task
from airflow.decorators.base import pull_value_from_bash_push as pull_value_from_bash_push, puller as puller, push as push, push_by_returning as push_by_returning
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import XComArg as XComArg, python_pull_from_bash as python_pull_from_bash
from airflow.operators.bash import BashOperator as BashOperator, bash_pull as bash_pull, bash_push as bash_push

value_1: list
value_2: dict
