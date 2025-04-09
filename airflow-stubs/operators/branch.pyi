from airflow.models import TaskInstance as TaskInstance
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.skipmixin import SkipMixin as SkipMixin
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils.context import Context as Context
from typing import Iterable

class BranchMixIn(SkipMixin):
    def do_branch(self, context: Context, branches_to_execute: str | Iterable[str]) -> str | Iterable[str]: ...

class BaseBranchOperator(BaseOperator, BranchMixIn):
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
    def execute(self, context: Context): ...
