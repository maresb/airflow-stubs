from airflow.decorators import task as task
from airflow.models.dag import dag as dag, tutorial_dag as tutorial_dag
from airflow.operators.python import is_venv_installed as is_venv_installed

def tutorial_taskflow_api_virtualenv(*args, **kwargs): ...
