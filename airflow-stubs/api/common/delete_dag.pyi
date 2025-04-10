from _typeshed import Incomplete
from airflow import models as models
from airflow.exceptions import AirflowException as AirflowException, DagNotFound as DagNotFound
from airflow.models import DagModel as DagModel, TaskFail as TaskFail
from airflow.models.errors import ParseImportError as ParseImportError
from airflow.models.serialized_dag import SerializedDagModel as SerializedDagModel
from airflow.utils.db import get_sqla_model_classes as get_sqla_model_classes
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session

log: Incomplete

def delete_dag(dag_id: str, keep_records_in_log: bool = True, session: Session = ...) -> int: ...
