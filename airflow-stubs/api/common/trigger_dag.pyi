from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import DagNotFound as DagNotFound, DagRunAlreadyExists as DagRunAlreadyExists
from airflow.models import DagBag as DagBag, DagModel as DagModel, DagRun as DagRun
from airflow.utils import timezone as timezone
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType
from datetime import datetime
from sqlalchemy.orm.session import Session as Session

def trigger_dag(dag_id: str, run_id: str | None = None, conf: dict | str | None = None, execution_date: datetime | None = None, replace_microseconds: bool = True, session: Session = ...) -> DagRun | None: ...
