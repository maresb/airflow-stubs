from _typeshed import Incomplete
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.operators.python import is_venv_installed as is_venv_installed
from airflow.utils.edgemodifier import Label as Label
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

PATH_TO_PYTHON_BINARY: Incomplete
run_this_first: Incomplete
options: Incomplete

def branching(choices: list[str]) -> str: ...

random_choice_instance: Incomplete
join: Incomplete

def some_task() -> None: ...

t: Incomplete
empty: Incomplete

def branching_ext_python(choices) -> str: ...

random_choice_ext_py: Incomplete
join_ext_py: Incomplete

def some_ext_py_task() -> None: ...

VENV_CACHE_PATH: Incomplete

def branching_virtualenv(choices) -> str: ...

random_choice_venv: Incomplete
join_venv: Incomplete

def some_venv_task() -> None: ...
