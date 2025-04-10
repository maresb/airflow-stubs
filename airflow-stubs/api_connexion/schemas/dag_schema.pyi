from _typeshed import Incomplete
from airflow import DAG as DAG
from airflow.api_connexion.schemas.common_schema import ScheduleIntervalSchema as ScheduleIntervalSchema, TimeDeltaSchema as TimeDeltaSchema, TimezoneField as TimezoneField
from airflow.configuration import conf as conf
from airflow.models.dag import DagModel as DagModel, DagTag as DagTag
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class DagTagSchema(SQLAlchemySchema):
    class Meta:
        model = DagTag
    name: Incomplete

class DAGSchema(SQLAlchemySchema):
    class Meta:
        model = DagModel
    dag_id: Incomplete
    dag_display_name: Incomplete
    root_dag_id: Incomplete
    is_paused: Incomplete
    is_active: Incomplete
    is_subdag: Incomplete
    last_parsed_time: Incomplete
    last_pickled: Incomplete
    last_expired: Incomplete
    scheduler_lock: Incomplete
    pickle_id: Incomplete
    default_view: Incomplete
    fileloc: Incomplete
    file_token: Incomplete
    owners: Incomplete
    description: Incomplete
    schedule_interval: Incomplete
    timetable_description: Incomplete
    tags: Incomplete
    max_active_tasks: Incomplete
    max_active_runs: Incomplete
    max_consecutive_failed_dag_runs: Incomplete
    has_task_concurrency_limits: Incomplete
    has_import_errors: Incomplete
    next_dagrun: Incomplete
    next_dagrun_data_interval_start: Incomplete
    next_dagrun_data_interval_end: Incomplete
    next_dagrun_create_after: Incomplete
    @staticmethod
    def get_owners(obj: DagModel): ...
    @staticmethod
    def get_token(obj: DagModel): ...

class DAGDetailSchema(DAGSchema):
    owners: Incomplete
    timezone: Incomplete
    catchup: Incomplete
    orientation: Incomplete
    concurrency: Incomplete
    max_active_tasks: Incomplete
    dataset_expression: Incomplete
    start_date: Incomplete
    dag_run_timeout: Incomplete
    doc_md: Incomplete
    default_view: Incomplete
    params: Incomplete
    tags: Incomplete
    is_paused: Incomplete
    is_active: Incomplete
    is_paused_upon_creation: Incomplete
    end_date: Incomplete
    template_searchpath: Incomplete
    render_template_as_native_obj: Incomplete
    last_loaded: Incomplete
    @staticmethod
    def get_concurrency(obj: DAG): ...
    @staticmethod
    def get_tags(obj: DAG): ...
    @staticmethod
    def get_owners(obj: DAG): ...
    @staticmethod
    def get_is_paused(obj: DAG): ...
    @staticmethod
    def get_is_active(obj: DAG): ...
    @staticmethod
    def get_params(obj: DAG): ...

class DAGCollection(NamedTuple):
    dags: list[DagModel]
    total_entries: int

class DAGCollectionSchema(Schema):
    dags: Incomplete
    total_entries: Incomplete

dags_collection_schema: Incomplete
dag_schema: Incomplete
dag_detail_schema: Incomplete
