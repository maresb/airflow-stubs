from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.operators.python import ExternalPythonOperator as ExternalPythonOperator, PythonOperator as PythonOperator, PythonVirtualenvOperator as PythonVirtualenvOperator, external_python_task as external_python_task, is_venv_installed as is_venv_installed, log_the_sql as log_the_sql, run_this as run_this, sleeping_task as sleeping_task, virtualenv_task as virtualenv_task

PATH_TO_PYTHON_BINARY: str
def print_context(ds: Incomplete | None = ..., **kwargs): ...
def log_sql(**kwargs): ...
def my_sleeping_function(random_base): ...

i: int
def callable_virtualenv(): ...
def callable_external_python(): ...
