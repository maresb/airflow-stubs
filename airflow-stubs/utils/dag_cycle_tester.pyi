from airflow.exceptions import AirflowDagCycleException as AirflowDagCycleException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.dag import DAG as DAG

CYCLE_NEW: int
CYCLE_IN_PROGRESS: int
CYCLE_DONE: int

def test_cycle(dag: DAG) -> None: ...
def check_cycle(dag: DAG) -> None: ...
