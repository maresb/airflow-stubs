from _typeshed import Incomplete
from marshmallow import Schema

class BaseInfoSchema(Schema):
    status: Incomplete

class MetaDatabaseInfoSchema(BaseInfoSchema): ...

class SchedulerInfoSchema(BaseInfoSchema):
    latest_scheduler_heartbeat: Incomplete

class TriggererInfoSchema(BaseInfoSchema):
    latest_triggerer_heartbeat: Incomplete

class DagProcessorInfoSchema(BaseInfoSchema):
    latest_dag_processor_heartbeat: Incomplete

class HealthInfoSchema(Schema):
    metadatabase: Incomplete
    scheduler: Incomplete
    triggerer: Incomplete
    dag_processor: Incomplete

health_schema: Incomplete
