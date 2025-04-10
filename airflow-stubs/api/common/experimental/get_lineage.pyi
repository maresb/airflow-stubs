import datetime
from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag, check_and_get_dagrun as check_and_get_dagrun
from airflow.lineage import PIPELINE_INLETS as PIPELINE_INLETS, PIPELINE_OUTLETS as PIPELINE_OUTLETS
from airflow.models.xcom import XCom as XCom
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session
from typing import Any

def get_lineage(dag_id: str, execution_date: datetime.datetime, *, session: Session = ...) -> dict[str, dict[str, Any]]: ...
