from _typeshed import Incomplete
from airflow.utils.state import State as State
from marshmallow import fields

class DagStateField(fields.String):
    validators: Incomplete
    def __init__(self, **metadata) -> None: ...

class TaskInstanceStateField(fields.String):
    validators: Incomplete
    def __init__(self, **metadata) -> None: ...
