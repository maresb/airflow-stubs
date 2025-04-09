import jsonschema
from airflow.exceptions import AirflowException as AirflowException
from airflow.settings import json as json
from airflow.typing_compat import Protocol as Protocol
from typing import Iterable

class Validator(Protocol):
    def is_valid(self, instance) -> bool: ...
    def validate(self, instance) -> None: ...
    def iter_errors(self, instance) -> Iterable[jsonschema.exceptions.ValidationError]: ...

def load_dag_schema_dict() -> dict: ...
def load_dag_schema() -> Validator: ...
