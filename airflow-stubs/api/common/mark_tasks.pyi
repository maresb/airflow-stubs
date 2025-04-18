from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.operator import Operator as Operator
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.operators.subdag import SubDagOperator as SubDagOperator
from airflow.utils import timezone as timezone
from airflow.utils.helpers import exactly_one as exactly_one
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from collections.abc import Generator
from datetime import datetime
from sqlalchemy.orm import Session as SASession
from typing import Collection, Iterable, NamedTuple

class _DagRunInfo(NamedTuple):
    logical_date: datetime
    data_interval: tuple[datetime, datetime]

def set_state(*, tasks: Collection[Operator | tuple[Operator, int]], run_id: str | None = None, execution_date: datetime | None = None, upstream: bool = False, downstream: bool = False, future: bool = False, past: bool = False, state: TaskInstanceState = ..., commit: bool = False, session: SASession = ...) -> list[TaskInstance]: ...
def all_subdag_tasks_query(sub_dag_run_ids: list[str], session: SASession, state: TaskInstanceState, confirmed_dates: Iterable[datetime]): ...
def get_all_dag_task_query(dag: DAG, session: SASession, state: TaskInstanceState, task_ids: list[str | tuple[str, int]], run_ids: Iterable[str]): ...
def verify_dagruns(dag_runs: Iterable[DagRun], commit: bool, state: DagRunState, session: SASession, current_task: Operator): ...
def find_task_relatives(tasks, downstream, upstream) -> Generator[Incomplete]: ...
def get_execution_dates(dag: DAG, execution_date: datetime, future: bool, past: bool, *, session: SASession = ...) -> list[datetime]: ...
def get_run_ids(dag: DAG, run_id: str, future: bool, past: bool, session: SASession = ...): ...
def set_dag_run_state_to_success(*, dag: DAG, execution_date: datetime | None = None, run_id: str | None = None, commit: bool = False, session: SASession = ...) -> list[TaskInstance]: ...
def set_dag_run_state_to_failed(*, dag: DAG, execution_date: datetime | None = None, run_id: str | None = None, commit: bool = False, session: SASession = ...) -> list[TaskInstance]: ...
def set_dag_run_state_to_running(*, dag: DAG, execution_date: datetime | None = None, run_id: str | None = None, commit: bool = False, session: SASession = ...) -> list[TaskInstance]: ...
def set_dag_run_state_to_queued(*, dag: DAG, execution_date: datetime | None = None, run_id: str | None = None, commit: bool = False, session: SASession = ...) -> list[TaskInstance]: ...
