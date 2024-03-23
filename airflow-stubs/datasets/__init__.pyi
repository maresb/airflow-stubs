from . import manager as manager
from _typeshed import Incomplete
from typing import Any, ClassVar as _ClassVar

class Dataset:
    __version__: _ClassVar[int] = ...
    __attrs_attrs__: _ClassVar[DatasetAttributes] = ...
    __attrs_own_setattr__: _ClassVar[bool] = ...
    extra: Incomplete
    uri: Incomplete
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __setattr__(self, name, val): ...
    def __init__(self, uri: str, extra: dict[str, Any] | None = ...) -> None: ...
