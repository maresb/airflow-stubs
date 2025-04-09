from _typeshed import Incomplete
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.bash import BashOperator as BashOperator

def my_py_command(params, test_mode: Incomplete | None = None, task: Incomplete | None = None): ...
def print_env_vars(test_mode: Incomplete | None = None) -> None: ...

run_this: Incomplete
my_command: Incomplete
also_run_this: Incomplete
env_var_test_task: Incomplete
