from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag, check_and_get_dagrun as check_and_get_dagrun
from airflow.models.xcom import XCom as XCom
from airflow.utils.session import provide_session as provide_session
from typing import Any

TYPE_CHECKING: bool
PIPELINE_INLETS: str
PIPELINE_OUTLETS: str
NEW_SESSION: None
def get_lineage(*args, **kwargs) -> dict[str, dict[str, Any]]: ...
