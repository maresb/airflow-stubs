from _typeshed import Incomplete
from airflow.models import Trigger as Trigger
from marshmallow_sqlalchemy import SQLAlchemySchema

class TriggerSchema(SQLAlchemySchema):
    class Meta:
        model = Trigger
    id: Incomplete
    classpath: Incomplete
    kwargs: Incomplete
    created_date: Incomplete
    triggerer_id: Incomplete
    @staticmethod
    def get_kwars(trigger: Trigger) -> str: ...
