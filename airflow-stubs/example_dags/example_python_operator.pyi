from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.operators.python import ExternalPythonOperator as ExternalPythonOperator, PythonOperator as PythonOperator, PythonVirtualenvOperator as PythonVirtualenvOperator, is_venv_installed as is_venv_installed

log: Incomplete
PATH_TO_PYTHON_BINARY: Incomplete

def print_context(ds: Incomplete | None = None, **kwargs): ...

run_this: Incomplete

def log_sql(**kwargs) -> None: ...

log_the_sql: Incomplete

def my_sleeping_function(random_base) -> None: ...

sleeping_task: Incomplete

def callable_virtualenv() -> None: ...

virtualenv_task: Incomplete

def callable_external_python() -> None: ...

external_python_task: Incomplete
