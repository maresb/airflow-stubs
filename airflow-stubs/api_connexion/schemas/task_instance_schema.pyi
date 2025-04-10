from _typeshed import Incomplete
from airflow.api_connexion.parameters import validate_istimezone as validate_istimezone
from airflow.api_connexion.schemas.common_schema import JsonObjectField as JsonObjectField
from airflow.api_connexion.schemas.enum_schemas import TaskInstanceStateField as TaskInstanceStateField
from airflow.api_connexion.schemas.job_schema import JobSchema as JobSchema
from airflow.api_connexion.schemas.sla_miss_schema import SlaMissSchema as SlaMissSchema
from airflow.api_connexion.schemas.trigger_schema import TriggerSchema as TriggerSchema
from airflow.models import SlaMiss as SlaMiss, TaskInstance as TaskInstance
from airflow.models.taskinstancehistory import TaskInstanceHistory as TaskInstanceHistory
from airflow.utils.helpers import exactly_one as exactly_one
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class TaskInstanceSchema(SQLAlchemySchema):
    class Meta:
        model = TaskInstance
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    execution_date: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    state: Incomplete
    try_number: Incomplete
    max_tries: Incomplete
    task_display_name: Incomplete
    hostname: Incomplete
    unixname: Incomplete
    pool: Incomplete
    pool_slots: Incomplete
    queue: Incomplete
    priority_weight: Incomplete
    operator: Incomplete
    queued_dttm: Incomplete
    pid: Incomplete
    executor: Incomplete
    executor_config: Incomplete
    note: Incomplete
    sla_miss: Incomplete
    rendered_map_index: Incomplete
    rendered_fields: Incomplete
    trigger: Incomplete
    triggerer_job: Incomplete
    def get_attribute(self, obj, attr, default): ...

class TaskInstanceHistorySchema(SQLAlchemySchema):
    class Meta:
        model = TaskInstanceHistory
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    state: Incomplete
    try_number: Incomplete
    max_tries: Incomplete
    task_display_name: Incomplete
    hostname: Incomplete
    unixname: Incomplete
    pool: Incomplete
    pool_slots: Incomplete
    queue: Incomplete
    priority_weight: Incomplete
    operator: Incomplete
    queued_dttm: Incomplete
    pid: Incomplete
    executor: Incomplete
    executor_config: Incomplete

class TaskInstanceCollection(NamedTuple):
    task_instances: list[tuple[TaskInstance, SlaMiss | None]]
    total_entries: int

class TaskInstanceCollectionSchema(Schema):
    task_instances: Incomplete
    total_entries: Incomplete

class TaskInstanceHistoryCollection(NamedTuple):
    task_instances: list[TaskInstanceHistory | None]
    total_entries: int

class TaskInstanceHistoryCollectionSchema(Schema):
    task_instances: Incomplete
    total_entries: Incomplete

class TaskInstanceBatchFormSchema(Schema):
    page_offset: Incomplete
    page_limit: Incomplete
    dag_ids: Incomplete
    dag_run_ids: Incomplete
    task_ids: Incomplete
    execution_date_gte: Incomplete
    execution_date_lte: Incomplete
    start_date_gte: Incomplete
    start_date_lte: Incomplete
    end_date_gte: Incomplete
    end_date_lte: Incomplete
    duration_gte: Incomplete
    duration_lte: Incomplete
    state: Incomplete
    pool: Incomplete
    queue: Incomplete
    executor: Incomplete

class ClearTaskInstanceFormSchema(Schema):
    dry_run: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    only_failed: Incomplete
    only_running: Incomplete
    include_subdags: Incomplete
    include_parentdag: Incomplete
    reset_dag_runs: Incomplete
    task_ids: Incomplete
    dag_run_id: Incomplete
    include_upstream: Incomplete
    include_downstream: Incomplete
    include_future: Incomplete
    include_past: Incomplete
    def validate_form(self, data, **kwargs) -> None: ...

class SetTaskInstanceStateFormSchema(Schema):
    dry_run: Incomplete
    task_id: Incomplete
    execution_date: Incomplete
    dag_run_id: Incomplete
    include_upstream: Incomplete
    include_downstream: Incomplete
    include_future: Incomplete
    include_past: Incomplete
    new_state: Incomplete
    def validate_form(self, data, **kwargs) -> None: ...

class SetSingleTaskInstanceStateFormSchema(Schema):
    dry_run: Incomplete
    new_state: Incomplete

class TaskInstanceReferenceSchema(Schema):
    task_id: Incomplete
    run_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete

class TaskInstanceReferenceCollection(NamedTuple):
    task_instances: list[tuple[TaskInstance, str]]

class TaskInstanceReferenceCollectionSchema(Schema):
    task_instances: Incomplete

class SetTaskInstanceNoteFormSchema(Schema):
    map_index: Incomplete
    note: Incomplete

class TaskDependencySchema(Schema):
    name: Incomplete
    reason: Incomplete

class TaskDependencyCollectionSchema(Schema):
    dependencies: Incomplete

task_instance_schema: Incomplete
task_instance_collection_schema: Incomplete
task_dependencies_collection_schema: Incomplete
task_instance_batch_form: Incomplete
clear_task_instance_form: Incomplete
set_task_instance_state_form: Incomplete
set_single_task_instance_state_form: Incomplete
task_instance_reference_schema: Incomplete
task_instance_reference_collection_schema: Incomplete
set_task_instance_note_form_schema: Incomplete
task_instance_history_schema: Incomplete
task_instance_history_collection_schema: Incomplete
