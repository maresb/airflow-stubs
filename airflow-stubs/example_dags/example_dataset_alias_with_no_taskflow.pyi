from _typeshed import Incomplete
from airflow import DAG as DAG
from airflow.datasets import Dataset as Dataset, DatasetAlias as DatasetAlias
from airflow.operators.python import PythonOperator as PythonOperator

def produce_dataset_events() -> None: ...
def produce_dataset_events_through_dataset_alias_with_no_taskflow(*, outlet_events: Incomplete | None = None) -> None: ...
def consume_dataset_event() -> None: ...
def consume_dataset_event_from_dataset_alias(*, inlet_events: Incomplete | None = None) -> None: ...
