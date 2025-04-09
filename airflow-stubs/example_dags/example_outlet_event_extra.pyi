from _typeshed import Incomplete
from airflow.datasets import Dataset as Dataset
from airflow.datasets.metadata import Metadata as Metadata
from airflow.decorators import task as task
from airflow.models.dag import DAG as DAG
from airflow.operators.bash import BashOperator as BashOperator
from collections.abc import Generator

ds: Incomplete

def dataset_with_extra_by_yield() -> Generator[Incomplete]: ...
def dataset_with_extra_by_context(*, outlet_events: Incomplete | None = None) -> None: ...
