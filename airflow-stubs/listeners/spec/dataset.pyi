from _typeshed import Incomplete
from airflow.datasets import Dataset as Dataset

hookspec: Incomplete

def on_dataset_created(dataset: Dataset): ...
def on_dataset_changed(dataset: Dataset): ...
