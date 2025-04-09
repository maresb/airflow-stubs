from _typeshed import Incomplete
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.bash import BashOperator as BashOperator

log: Incomplete

def generate_value(): ...
def print_value(value, ts: Incomplete | None = None) -> None: ...

bash_op1: Incomplete
bash_op2: Incomplete
xcom_args_a: Incomplete
xcom_args_b: Incomplete
