from _typeshed import Incomplete
from enum import Enum

class JobState(str, Enum):
    RUNNING = 'running'
    SUCCESS = 'success'
    RESTARTING = 'restarting'
    FAILED = 'failed'

class TaskInstanceState(str, Enum):
    REMOVED = 'removed'
    SCHEDULED = 'scheduled'
    QUEUED = 'queued'
    RUNNING = 'running'
    SUCCESS = 'success'
    RESTARTING = 'restarting'
    FAILED = 'failed'
    UP_FOR_RETRY = 'up_for_retry'
    UP_FOR_RESCHEDULE = 'up_for_reschedule'
    UPSTREAM_FAILED = 'upstream_failed'
    SKIPPED = 'skipped'
    DEFERRED = 'deferred'
    SHUTDOWN = 'shutdown'

class DagRunState(str, Enum):
    QUEUED = 'queued'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'

class State:
    SUCCESS: Incomplete
    RUNNING: Incomplete
    FAILED: Incomplete
    NONE: Incomplete
    REMOVED: Incomplete
    SCHEDULED: Incomplete
    QUEUED: Incomplete
    RESTARTING: Incomplete
    UP_FOR_RETRY: Incomplete
    UP_FOR_RESCHEDULE: Incomplete
    UPSTREAM_FAILED: Incomplete
    SKIPPED: Incomplete
    DEFERRED: Incomplete
    SHUTDOWN: Incomplete
    finished_dr_states: frozenset[DagRunState]
    unfinished_dr_states: frozenset[DagRunState]
    task_states: tuple[TaskInstanceState | None, ...]
    dag_states: tuple[DagRunState, ...]
    state_color: dict[TaskInstanceState | None, str]
    @classmethod
    def color(cls, state): ...
    @classmethod
    def color_fg(cls, state): ...
    finished: frozenset[TaskInstanceState]
    unfinished: frozenset[TaskInstanceState | None]
    failed_states: frozenset[TaskInstanceState]
    success_states: frozenset[TaskInstanceState]
    terminating_states: Incomplete
    adoptable_states: Incomplete
