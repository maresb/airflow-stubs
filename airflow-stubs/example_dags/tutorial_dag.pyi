from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.operators.python import PythonOperator as PythonOperator

def extract(**kwargs) -> None: ...
def transform(**kwargs) -> None: ...
def load(**kwargs) -> None: ...

extract_task: Incomplete
transform_task: Incomplete
load_task: Incomplete
