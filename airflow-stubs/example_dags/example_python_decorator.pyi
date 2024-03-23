from airflow.decorators import task as task
from airflow.models.dag import dag as dag
from airflow.operators.python import is_venv_installed as is_venv_installed

PATH_TO_PYTHON_BINARY: str
def example_python_decorator(*args, **kwargs): ...
