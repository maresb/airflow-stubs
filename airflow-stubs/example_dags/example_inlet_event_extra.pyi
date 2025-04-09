from _typeshed import Incomplete
from airflow.datasets import Dataset as Dataset
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.bash import BashOperator as BashOperator

ds: Incomplete

def read_dataset_event(*, inlet_events: Incomplete | None = None) -> None: ...
