from _typeshed import Incomplete
from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowClusterPolicyError as AirflowClusterPolicyError, AirflowClusterPolicySkipDag as AirflowClusterPolicySkipDag, AirflowClusterPolicyViolation as AirflowClusterPolicyViolation, AirflowDagCycleException as AirflowDagCycleException, AirflowDagDuplicatedIdException as AirflowDagDuplicatedIdException, AirflowException as AirflowException, AirflowTaskTimeout as AirflowTaskTimeout, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models.base import Base as Base
from airflow.models.dag import DAG as DAG
from airflow.stats import Stats as Stats
from airflow.utils import timezone as timezone
from airflow.utils.dag_cycle_tester import check_cycle as check_cycle
from airflow.utils.docs import get_docs_url as get_docs_url
from airflow.utils.file import correct_maybe_zipped as correct_maybe_zipped, get_unique_dag_module_name as get_unique_dag_module_name, list_py_file_paths as list_py_file_paths, might_contain_dag as might_contain_dag
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.retries import MAX_DB_RETRIES as MAX_DB_RETRIES, run_with_db_retries as run_with_db_retries
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.timeout import timeout as timeout
from airflow.utils.types import ArgNotSet as ArgNotSet, NOTSET as NOTSET
from airflow.utils.warnings import capture_with_reraise as capture_with_reraise
from datetime import datetime, timedelta
from pathlib import Path
from sqlalchemy.orm import Session as Session
from typing import NamedTuple

class FileLoadStat(NamedTuple):
    file: str
    duration: timedelta
    dag_num: int
    task_num: int
    dags: str
    warning_num: int

class DagBag(LoggingMixin):
    dag_folder: Incomplete
    dags: dict[str, DAG]
    file_last_changed: dict[str, datetime]
    import_errors: dict[str, str]
    captured_warnings: dict[str, tuple[str, ...]]
    has_logged: bool
    read_dags_from_db: Incomplete
    dags_last_fetched: dict[str, datetime]
    dags_hash: dict[str, str]
    dagbag_import_error_tracebacks: Incomplete
    dagbag_import_error_traceback_depth: Incomplete
    load_op_links: Incomplete
    def __init__(self, dag_folder: str | Path | None = None, include_examples: bool | ArgNotSet = ..., safe_mode: bool | ArgNotSet = ..., read_dags_from_db: bool = False, store_serialized_dags: bool | None = None, load_op_links: bool = True, collect_dags: bool = True) -> None: ...
    def size(self) -> int: ...
    @property
    def store_serialized_dags(self) -> bool: ...
    @property
    def dag_ids(self) -> list[str]: ...
    def get_dag(self, dag_id, session: Session = None): ...
    def process_file(self, filepath, only_if_updated: bool = True, safe_mode: bool = True): ...
    def bag_dag(self, dag, root_dag) -> None: ...
    dagbag_stats: Incomplete
    def collect_dags(self, dag_folder: str | Path | None = None, only_if_updated: bool = True, include_examples: bool = ..., safe_mode: bool = ...): ...
    def collect_dags_from_db(self) -> None: ...
    def dagbag_report(self): ...
    def sync_to_db(self, processor_subdir: str | None = None, session: Session = ...): ...

def generate_md5_hash(context): ...

class DagPriorityParsingRequest(Base):
    __tablename__: str
    id: Incomplete
    fileloc: Incomplete
    def __init__(self, fileloc: str) -> None: ...
