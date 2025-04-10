from _typeshed import Incomplete
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.models.xcom_arg import XComArg as XComArg
from airflow.operators.bash import BashOperator as BashOperator

value_1: Incomplete
value_2: Incomplete

def push(ti: Incomplete | None = None) -> None: ...
def push_by_returning(): ...
def puller(pulled_value_2, ti: Incomplete | None = None) -> None: ...
def pull_value_from_bash_push(ti: Incomplete | None = None) -> None: ...

bash_push: Incomplete
bash_pull: Incomplete
python_pull_from_bash: Incomplete
