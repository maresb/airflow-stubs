from _typeshed import Incomplete
from airflow.models import SlaMiss as SlaMiss
from marshmallow_sqlalchemy import SQLAlchemySchema

class SlaMissSchema(SQLAlchemySchema):
    class Meta:
        model = SlaMiss
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    email_sent: Incomplete
    timestamp: Incomplete
    description: Incomplete
    notification_sent: Incomplete
