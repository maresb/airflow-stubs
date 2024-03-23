from airflow.jobs.job import Job as Job, most_recent_job as most_recent_job
from airflow.serialization.serialized_objects import BaseSerialization as BaseSerialization
from airflow.utils.session import create_session as create_session
from typing import Any

TYPE_CHECKING: bool
def internal_airflow_api(body: dict[str, Any]) -> APIResponse: ...
