from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.models import Operator as Operator
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.dag import DAG as DAG, DagModel as DagModel
from airflow.models.dagcode import DagCode as DagCode
from airflow.models.dagrun import DagRun as DagRun
from airflow.serialization.dag_dependency import DagDependency as DagDependency
from airflow.serialization.serialized_objects import SerializedDAG as SerializedDAG
from airflow.settings import COMPRESS_SERIALIZED_DAGS as COMPRESS_SERIALIZED_DAGS, MIN_SERIALIZED_DAG_UPDATE_INTERVAL as MIN_SERIALIZED_DAG_UPDATE_INTERVAL, json as json
from airflow.utils import timezone as timezone
from airflow.utils.hashlib_wrapper import md5 as md5
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from datetime import datetime
from sqlalchemy.orm import Session as Session
from typing import Collection

log: Incomplete

class SerializedDagModel(Base):
    __tablename__: str
    dag_id: Incomplete
    fileloc: Incomplete
    fileloc_hash: Incomplete
    last_updated: Incomplete
    dag_hash: Incomplete
    processor_subdir: Incomplete
    __table_args__: Incomplete
    dag_runs: Incomplete
    dag_model: Incomplete
    load_op_links: bool
    def __init__(self, dag: DAG, processor_subdir: str | None = None) -> None: ...
    @classmethod
    def write_dag(cls, dag: DAG, min_update_interval: int | None = None, processor_subdir: str | None = None, session: Session = ...) -> bool: ...
    @classmethod
    def read_all_dags(cls, session: Session = ...) -> dict[str, SerializedDAG]: ...
    @property
    def data(self) -> dict | None: ...
    @property
    def dag(self) -> SerializedDAG: ...
    @classmethod
    def remove_dag(cls, dag_id: str, session: Session = ...) -> None: ...
    @classmethod
    def remove_deleted_dags(cls, alive_dag_filelocs: Collection[str], processor_subdir: str | None = None, session: Session = ...) -> None: ...
    @classmethod
    def has_dag(cls, dag_id: str, session: Session = ...) -> bool: ...
    @classmethod
    def get_dag(cls, dag_id: str, session: Session = ...) -> SerializedDAG | None: ...
    @classmethod
    def get(cls, dag_id: str, session: Session = ...) -> SerializedDagModel | None: ...
    @staticmethod
    def bulk_sync_to_db(dags: list[DAG], processor_subdir: str | None = None, session: Session = ...) -> None: ...
    @classmethod
    def get_last_updated_datetime(cls, dag_id: str, session: Session = ...) -> datetime | None: ...
    @classmethod
    def get_max_last_updated_datetime(cls, session: Session = ...) -> datetime | None: ...
    @classmethod
    def get_latest_version_hash(cls, dag_id: str, session: Session = ...) -> str | None: ...
    @classmethod
    def get_latest_version_hash_and_updated_datetime(cls, dag_id: str, *, session: Session) -> tuple[str, datetime] | None: ...
    @classmethod
    def get_dag_dependencies(cls, session: Session = ...) -> dict[str, list[DagDependency]]: ...
    @staticmethod
    def get_serialized_dag(dag_id: str, task_id: str, session: Session = ...) -> Operator | None: ...
