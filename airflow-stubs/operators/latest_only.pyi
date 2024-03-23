import airflow.operators.branch
from airflow.operators.branch import BaseBranchOperator as BaseBranchOperator
from typing import ClassVar, Iterable

TYPE_CHECKING: bool

class LatestOnlyOperator(airflow.operators.branch.BaseBranchOperator):
    ui_color: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
    def __init__(self, *args, **kwargs) -> None: ...
