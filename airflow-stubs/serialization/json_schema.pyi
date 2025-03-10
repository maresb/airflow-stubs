import jsonschema.exceptions
import typing
from airflow.exceptions import AirflowException as AirflowException
from typing import ClassVar, Iterable

TYPE_CHECKING: bool

class Validator(typing.Protocol):
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def is_valid(self, instance) -> bool: ...
    def validate(self, instance) -> None: ...
    def iter_errors(self, instance) -> Iterable[jsonschema.exceptions.ValidationError]: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...
def load_dag_schema_dict() -> dict: ...
def load_dag_schema() -> Validator: ...
