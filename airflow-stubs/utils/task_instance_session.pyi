from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.settings import TracebackSession as TracebackSession
from sqlalchemy.orm import Session as Session

log: Incomplete

def get_current_task_instance_session() -> Session: ...
def set_current_task_instance_session(session: Session): ...
