from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.utils.session import provide_session as provide_session
from sqlalchemy.orm import Session as Session
from typing import Any, Iterator, NamedTuple

class BaseTIDep:
    IGNORABLE: bool
    IS_TASK_DEP: bool
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def name(self) -> str: ...
    def get_dep_statuses(self, ti: TaskInstance, session: Session, dep_context: DepContext | None = None) -> Iterator[TIDepStatus]: ...
    def is_met(self, ti: TaskInstance, session: Session, dep_context: DepContext | None = None) -> bool: ...
    def get_failure_reasons(self, ti: TaskInstance, session: Session, dep_context: DepContext | None = None) -> Iterator[str]: ...

class TIDepStatus(NamedTuple):
    dep_name: str
    passed: bool
    reason: str
