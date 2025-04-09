from airflow.exceptions import AirflowException as AirflowException
from airflow.jobs.job import Job as Job
from airflow.serialization.pydantic.job import JobPydantic as JobPydantic
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

class BaseJobRunner:
    job_type: str
    job: Job
    def __init__(self, job: Job) -> None: ...
    def heartbeat_callback(self, session: Session = ...) -> None: ...
    @classmethod
    def most_recent_job(cls, session: Session = ...) -> Job | JobPydantic | None: ...
