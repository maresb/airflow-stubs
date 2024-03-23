from typing import ClassVar as _ClassVar

class File:
    template_fields: _ClassVar[tuple] = ...
    __attrs_attrs__: _ClassVar[FileAttributes] = ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __init__(self, url: str, type_hint: str | None = ...) -> None: ...

class User:
    template_fields: _ClassVar[tuple] = ...
    __attrs_attrs__: _ClassVar[UserAttributes] = ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __init__(self) -> None: ...

class Tag:
    template_fields: _ClassVar[tuple] = ...
    __attrs_attrs__: _ClassVar[TagAttributes] = ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __init__(self) -> None: ...

class Column:
    template_fields: _ClassVar[tuple] = ...
    __attrs_attrs__: _ClassVar[ColumnAttributes] = ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __init__(self) -> None: ...
def default_if_none(arg: bool | None) -> bool: ...

class Table:
    template_fields: _ClassVar[tuple] = ...
    __attrs_attrs__: _ClassVar[TableAttributes] = ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __init__(self) -> None: ...