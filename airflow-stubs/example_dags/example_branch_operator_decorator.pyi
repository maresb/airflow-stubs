from airflow.decorators import task as task
from airflow.decorators.base import branching as branching, branching_ext_python as branching_ext_python, branching_virtualenv as branching_virtualenv, some_ext_py_task as some_ext_py_task, some_task as some_task, some_venv_task as some_venv_task
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import random_choice_ext_py as random_choice_ext_py, random_choice_instance as random_choice_instance, random_choice_venv as random_choice_venv, t as t
from airflow.operators.empty import EmptyOperator as EmptyOperator, empty as empty, join as join, join_ext_py as join_ext_py, join_venv as join_venv, run_this_first as run_this_first
from airflow.operators.python import is_venv_installed as is_venv_installed
from airflow.utils.edgemodifier import Label as Label
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

PATH_TO_PYTHON_BINARY: str
options: list
option: str
VENV_CACHE_PATH: str
