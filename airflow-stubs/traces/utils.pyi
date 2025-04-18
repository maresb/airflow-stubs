from _typeshed import Incomplete
from airflow.models import DagRun as DagRun, TaskInstance as TaskInstance
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.traces import NO_TRACE_ID as NO_TRACE_ID
from airflow.utils.hashlib_wrapper import md5 as md5

TRACE_ID: int
SPAN_ID: int
log: Incomplete

def gen_trace_id(dag_run: DagRun, as_int: bool = False) -> str | int: ...
def gen_span_id_from_ti_key(ti_key: TaskInstanceKey, as_int: bool = False) -> str | int: ...
def gen_dag_span_id(dag_run: DagRun, as_int: bool = False) -> str | int: ...
def gen_span_id(ti: TaskInstance, as_int: bool = False) -> str | int: ...
def parse_traceparent(traceparent_str: str | None = None) -> dict: ...
def parse_tracestate(tracestate_str: str | None = None) -> dict: ...
def is_valid_trace_id(trace_id: str) -> bool: ...
def is_valid_span_id(span_id: str) -> bool: ...
