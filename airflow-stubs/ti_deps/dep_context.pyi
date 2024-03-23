from _typeshed import Incomplete
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.utils.state import State as State
from typing import ClassVar

TYPE_CHECKING: bool

class DepContext:
    __attrs_attrs__: ClassVar[DepContextAttributes] = ...
    __attrs_own_setattr__: ClassVar[bool] = ...
    deps: Incomplete
    description: Incomplete
    finished_tis: Incomplete
    flag_upstream_failed: Incomplete
    have_changed_ti_states: Incomplete
    ignore_all_deps: Incomplete
    ignore_depends_on_past: Incomplete
    ignore_in_reschedule_period: Incomplete
    ignore_in_retry_period: Incomplete
    ignore_task_deps: Incomplete
    ignore_ti_state: Incomplete
    ignore_unmapped_tasks: Incomplete
    wait_for_past_depends_before_skipping: Incomplete
    def ensure_finished_tis(self, dag_run: DagRun, session: Session) -> list[TaskInstance]: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __init__(self, deps: set = ..., flag_upstream_failed: bool = ..., ignore_all_deps: bool = ..., ignore_depends_on_past: bool = ..., wait_for_past_depends_before_skipping: bool = ..., ignore_in_retry_period: bool = ..., ignore_in_reschedule_period: bool = ..., ignore_task_deps: bool = ..., ignore_ti_state: bool = ..., ignore_unmapped_tasks: bool = ..., finished_tis: list[TaskInstance] | None = ..., description: str | None = ..., have_changed_ti_states: bool = ...) -> None: ...
