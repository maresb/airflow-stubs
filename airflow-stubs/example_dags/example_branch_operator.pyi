from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.operators.python import BranchExternalPythonOperator as BranchExternalPythonOperator, BranchPythonOperator as BranchPythonOperator, BranchPythonVirtualenvOperator as BranchPythonVirtualenvOperator, ExternalPythonOperator as ExternalPythonOperator, PythonOperator as PythonOperator, PythonVirtualenvOperator as PythonVirtualenvOperator, is_venv_installed as is_venv_installed
from airflow.utils.edgemodifier import Label as Label
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

PATH_TO_PYTHON_BINARY: Incomplete
run_this_first: Incomplete
options: Incomplete
branching: Incomplete
join: Incomplete
t: Incomplete
empty_follow: Incomplete

def branch_with_external_python(choices): ...

branching_ext_py: Incomplete
join_ext_py: Incomplete

def hello_world_with_external_python() -> None: ...

VENV_CACHE_PATH: Incomplete

def branch_with_venv(choices): ...

branching_venv: Incomplete
join_venv: Incomplete

def hello_world_with_venv() -> None: ...
