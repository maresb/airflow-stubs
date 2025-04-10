from _typeshed import Incomplete
from airflow.jobs.job import Job as Job
from marshmallow_sqlalchemy import SQLAlchemySchema

class JobSchema(SQLAlchemySchema):
    class Meta:
        model = Job
    id: Incomplete
    dag_id: Incomplete
    state: Incomplete
    job_type: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    latest_heartbeat: Incomplete
    executor_class: Incomplete
    hostname: Incomplete
    unixname: Incomplete
