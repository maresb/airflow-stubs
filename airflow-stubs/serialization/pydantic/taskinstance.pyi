import pendulum
from _typeshed import Incomplete
from airflow.exceptions import AirflowRescheduleException as AirflowRescheduleException, TaskDeferred as TaskDeferred
from airflow.models import Operator as Operator
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance, TaskReturnCode as TaskReturnCode
from airflow.serialization.pydantic.dag import DagModelPydantic as DagModelPydantic
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.utils.context import Context as Context
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict, PlainSerializer as PlainSerializer, PlainValidator as PlainValidator, ValidationInfo as ValidationInfo, is_pydantic_2_installed as is_pydantic_2_installed
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.xcom import XCOM_RETURN_KEY as XCOM_RETURN_KEY
from datetime import datetime
from sqlalchemy.orm import Session as Session
from typing import Any, Iterable

def serialize_operator(x: Operator | None) -> dict | None: ...
def validated_operator(x: dict[str, Any] | Operator, _info: ValidationInfo) -> Any: ...

PydanticOperator: Incomplete

class TaskInstancePydantic(BaseModelPydantic, LoggingMixin):
    task_id: str
    dag_id: str
    run_id: str
    map_index: int
    start_date: datetime | None
    end_date: datetime | None
    execution_date: datetime | None
    duration: float | None
    state: str | None
    try_number: int
    max_tries: int
    hostname: str
    unixname: str
    job_id: int | None
    pool: str
    pool_slots: int
    queue: str
    priority_weight: int | None
    operator: str
    custom_operator_name: str | None
    queued_dttm: datetime | None
    queued_by_job_id: int | None
    pid: int | None
    executor: str | None
    executor_config: Any
    updated_at: datetime | None
    rendered_map_index: str | None
    external_executor_id: str | None
    trigger_id: int | None
    trigger_timeout: datetime | None
    next_method: str | None
    next_kwargs: dict | None
    run_as_user: str | None
    task: PydanticOperator | None
    test_mode: bool
    dag_run: DagRunPydantic | None
    dag_model: DagModelPydantic | None
    raw: bool | None
    is_trigger_log_context: bool | None
    model_config: Incomplete
    def clear_xcom_data(self, session: Session | None = None): ...
    def set_state(self, state, session: Session | None = None) -> bool: ...
    def render_templates(self, context: Context | None = None, jinja_env: Incomplete | None = None): ...
    def init_run_context(self, raw: bool = False) -> None: ...
    def xcom_pull(self, task_ids: str | Iterable[str] | None = None, dag_id: str | None = None, key: str = ..., include_prior_dates: bool = False, session: Session | None = None, *, map_indexes: int | Iterable[int] | None = None, default: Any = None) -> Any: ...
    def xcom_push(self, key: str, value: Any, execution_date: datetime | None = None, session: Session | None = None) -> None: ...
    def get_dagrun(self, session: Session | None = None) -> DagRunPydantic: ...
    def refresh_from_db(self, session: Session | None = None, lock_for_update: bool = False) -> None: ...
    def set_duration(self) -> None: ...
    @property
    def stats_tags(self) -> dict[str, str]: ...
    def clear_next_method_args(self) -> None: ...
    def get_template_context(self, session: Session | None = None, ignore_param_exceptions: bool = True) -> Context: ...
    def is_eligible_to_retry(self): ...
    def handle_failure(self, error: None | str | BaseException, test_mode: bool | None = None, context: Context | None = None, force_fail: bool = False, session: Session | None = None) -> None: ...
    def refresh_from_task(self, task: Operator, pool_override: str | None = None) -> None: ...
    def get_previous_dagrun(self, state: DagRunState | None = None, session: Session | None = None) -> DagRun | None: ...
    def get_previous_execution_date(self, state: DagRunState | None = None, session: Session | None = None) -> pendulum.DateTime | None: ...
    def get_previous_start_date(self, state: DagRunState | None = None, session: Session | None = None) -> pendulum.DateTime | None: ...
    def email_alert(self, exception, task: BaseOperator) -> None: ...
    def get_email_subject_content(self, exception: BaseException, task: BaseOperator | None = None) -> tuple[str, str, str]: ...
    def get_previous_ti(self, state: DagRunState | None = None, session: Session | None = None) -> TaskInstance | TaskInstancePydantic | None: ...
    def check_and_change_state_before_execution(self, verbose: bool = True, ignore_all_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_task_deps: bool = False, ignore_ti_state: bool = False, mark_success: bool = False, test_mode: bool = False, job_id: str | None = None, pool: str | None = None, external_executor_id: str | None = None, session: Session | None = None) -> bool: ...
    def schedule_downstream_tasks(self, session: Session | None = None, max_tis_per_query: int | None = None): ...
    def command_as_list(self, mark_success: bool = False, ignore_all_deps: bool = False, ignore_task_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_ti_state: bool = False, local: bool = False, pickle_id: int | None = None, raw: bool = False, job_id: str | None = None, pool: str | None = None, cfg_path: str | None = None) -> list[str]: ...
    def defer_task(self, exception: TaskDeferred, session: Session | None = None): ...
    def get_relevant_upstream_map_indexes(self, upstream: Operator, ti_count: int | None, *, session: Session | None = None) -> int | range | None: ...
