import airflow.models.baseoperator
import airflow.models.skipmixin
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.skipmixin import SkipMixin as SkipMixin
from typing import ClassVar, Iterable

TYPE_CHECKING: bool

class BranchMixIn(airflow.models.skipmixin.SkipMixin):
    def do_branch(self, context: Context, branches_to_execute: str | Iterable[str]) -> str | Iterable[str]: ...

class BaseBranchOperator(airflow.models.baseoperator.BaseOperator, BranchMixIn):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
    def execute(self, context: Context): ...
    def __init__(self, *args, **kwargs) -> None: ...