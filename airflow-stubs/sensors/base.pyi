from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig, internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, AirflowFailException as AirflowFailException, AirflowRescheduleException as AirflowRescheduleException, AirflowSensorTimeout as AirflowSensorTimeout, AirflowSkipException as AirflowSkipException, AirflowTaskTimeout as AirflowTaskTimeout, TaskDeferralError as TaskDeferralError
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.skipmixin import SkipMixin as SkipMixin
from airflow.models.taskreschedule import TaskReschedule as TaskReschedule
from airflow.ti_deps.deps.ready_to_reschedule import ReadyToRescheduleDep as ReadyToRescheduleDep
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from airflow.utils.decorators import apply_defaults as apply_defaults
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from datetime import timedelta
from sqlalchemy.orm.session import Session as Session
from typing import Any, Iterable

class PokeReturnValue:
    xcom_value: Incomplete
    is_done: Incomplete
    def __init__(self, is_done: bool, xcom_value: Any | None = None) -> None: ...
    def __bool__(self) -> bool: ...

class BaseSensorOperator(BaseOperator, SkipMixin):
    ui_color: str
    valid_modes: Iterable[str]
    deps: Incomplete
    poke_interval: Incomplete
    soft_fail: Incomplete
    timeout: Incomplete
    mode: Incomplete
    exponential_backoff: Incomplete
    max_wait: Incomplete
    silent_fail: Incomplete
    never_fail: Incomplete
    def __init__(self, *, poke_interval: timedelta | float = 60, timeout: timedelta | float = ..., soft_fail: bool = False, mode: str = 'poke', exponential_backoff: bool = False, max_wait: timedelta | float | None = None, silent_fail: bool = False, never_fail: bool = False, **kwargs) -> None: ...
    def poke(self, context: Context) -> bool | PokeReturnValue: ...
    def execute(self, context: Context) -> Any: ...
    def resume_execution(self, next_method: str, next_kwargs: dict[str, Any] | None, context: Context): ...
    def prepare_for_execution(self) -> BaseOperator: ...
    @property
    def reschedule(self): ...
    @classmethod
    def get_serialized_fields(cls): ...

def poke_mode_only(cls): ...
