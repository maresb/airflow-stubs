from _typeshed import Incomplete
from airflow.api_connexion.schemas.common_schema import ClassReferenceSchema as ClassReferenceSchema, ColorField as ColorField, TimeDeltaSchema as TimeDeltaSchema, WeightRuleField as WeightRuleField
from airflow.api_connexion.schemas.dag_schema import DAGSchema as DAGSchema
from airflow.models.mappedoperator import MappedOperator as MappedOperator
from airflow.models.operator import Operator as Operator
from marshmallow import Schema
from typing import NamedTuple

class TaskSchema(Schema):
    class_ref: Incomplete
    operator_name: Incomplete
    task_id: Incomplete
    task_display_name: Incomplete
    owner: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    trigger_rule: Incomplete
    extra_links: Incomplete
    depends_on_past: Incomplete
    wait_for_downstream: Incomplete
    retries: Incomplete
    queue: Incomplete
    pool: Incomplete
    pool_slots: Incomplete
    execution_timeout: Incomplete
    retry_delay: Incomplete
    retry_exponential_backoff: Incomplete
    priority_weight: Incomplete
    weight_rule: Incomplete
    ui_color: Incomplete
    ui_fgcolor: Incomplete
    template_fields: Incomplete
    sub_dag: Incomplete
    downstream_task_ids: Incomplete
    params: Incomplete
    is_mapped: Incomplete
    doc_md: Incomplete

class TaskCollection(NamedTuple):
    tasks: list[Operator]
    total_entries: int

class TaskCollectionSchema(Schema):
    tasks: Incomplete
    total_entries: Incomplete

task_schema: Incomplete
task_collection_schema: Incomplete
