from . import get_lineage as get_lineage
from airflow.exceptions import DagNotFound as DagNotFound, DagRunNotFound as DagRunNotFound, TaskNotFound as TaskNotFound
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag

TYPE_CHECKING: bool
def check_and_get_dag(dag_id: str, task_id: str | None = ...) -> DagModel: ...
def check_and_get_dagrun(dag: DagModel, execution_date: datetime) -> DagRun: ...
