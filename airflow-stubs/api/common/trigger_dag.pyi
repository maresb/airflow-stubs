import airflow.utils.timezone as timezone
from airflow.exceptions import DagNotFound as DagNotFound, DagRunAlreadyExists as DagRunAlreadyExists
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType

TYPE_CHECKING: bool
def trigger_dag(dag_id: str, run_id: str | None = ..., conf: dict | str | None = ..., execution_date: datetime | None = ..., replace_microseconds: bool = ...) -> DagRun | None: ...
