from _typeshed import Incomplete
from airflow.api_connexion.schemas.enum_schemas import DagStateField as DagStateField
from marshmallow import Schema

class DagStatsStateSchema(Schema):
    state: Incomplete
    count: Incomplete

class DagStatsSchema(Schema):
    dag_id: Incomplete
    stats: Incomplete

class DagStatsCollectionSchema(Schema):
    dags: Incomplete
    total_entries: Incomplete

dag_stats_state_schema: Incomplete
dag_stats_schema: Incomplete
dag_stats_collection_schema: Incomplete
