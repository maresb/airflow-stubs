from _typeshed import Incomplete
from airflow.api_connexion.exceptions import BadRequest as BadRequest
from airflow.api_connexion.parameters import validate_istimezone as validate_istimezone
from airflow.api_connexion.schemas.enum_schemas import DagStateField as DagStateField
from airflow.models.dagrun import DagRun as DagRun
from airflow.utils import timezone as timezone
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType
from marshmallow import fields
from marshmallow.schema import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class ConfObject(fields.Field): ...

class DAGRunSchema(SQLAlchemySchema):
    class Meta:
        model = DagRun
        dateformat: str
    run_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    state: Incomplete
    external_trigger: Incomplete
    conf: Incomplete
    data_interval_start: Incomplete
    data_interval_end: Incomplete
    last_scheduling_decision: Incomplete
    run_type: Incomplete
    note: Incomplete
    def autogenerate(self, data, **kwargs): ...
    def autofill(self, data, **kwargs): ...
    def validate_data_interval_dates(self, data, **kwargs) -> None: ...

class SetDagRunStateFormSchema(Schema):
    state: Incomplete

class ClearDagRunStateFormSchema(Schema):
    dry_run: Incomplete

class DAGRunCollection(NamedTuple):
    dag_runs: list[DagRun]
    total_entries: int

class DAGRunCollectionSchema(Schema):
    dag_runs: Incomplete
    total_entries: Incomplete

class DagRunsBatchFormSchema(Schema):
    class Meta:
        datetimeformat: str
        strict: bool
    order_by: Incomplete
    page_offset: Incomplete
    page_limit: Incomplete
    dag_ids: Incomplete
    states: Incomplete
    execution_date_gte: Incomplete
    execution_date_lte: Incomplete
    start_date_gte: Incomplete
    start_date_lte: Incomplete
    end_date_gte: Incomplete
    end_date_lte: Incomplete
    updated_at_gte: Incomplete
    updated_at_lte: Incomplete

class SetDagRunNoteFormSchema(Schema):
    note: Incomplete

dagrun_schema: Incomplete
dagrun_collection_schema: Incomplete
set_dagrun_state_form_schema: Incomplete
clear_dagrun_form_schema: Incomplete
dagruns_batch_form_schema: Incomplete
set_dagrun_note_form_schema: Incomplete
