import marshmallow.fields
from airflow.utils.state import State as State
from typing import ClassVar

class DagStateField(marshmallow.fields.String):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    __slotnames__: ClassVar[list] = ...
    def __init__(self, **metadata) -> None: ...

class TaskInstanceStateField(marshmallow.fields.String):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    __slotnames__: ClassVar[list] = ...
    def __init__(self, **metadata) -> None: ...
