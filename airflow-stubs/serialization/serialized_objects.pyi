from _typeshed import Incomplete
from airflow import macros as macros
from airflow.callbacks.callback_requests import DagCallbackRequest as DagCallbackRequest, SlaCallbackRequest as SlaCallbackRequest, TaskCallbackRequest as TaskCallbackRequest
from airflow.compat.functools import cache as cache
from airflow.configuration import conf as conf
from airflow.datasets import BaseDataset as BaseDataset, Dataset as Dataset, DatasetAlias as DatasetAlias, DatasetAll as DatasetAll, DatasetAny as DatasetAny
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning, SerializationError as SerializationError, TaskDeferred as TaskDeferred
from airflow.jobs.job import Job as Job
from airflow.models import Trigger as Trigger
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.baseoperatorlink import BaseOperatorLink as BaseOperatorLink
from airflow.models.connection import Connection as Connection
from airflow.models.dag import DAG as DAG, DagModel as DagModel, create_timetable as create_timetable
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.expandinput import EXPAND_INPUT_EMPTY as EXPAND_INPUT_EMPTY, ExpandInput as ExpandInput, create_expand_input as create_expand_input, get_map_type_key as get_map_type_key
from airflow.models.mappedoperator import MappedOperator as MappedOperator
from airflow.models.operator import Operator as Operator
from airflow.models.param import Param as Param, ParamsDict as ParamsDict
from airflow.models.taskinstance import SimpleTaskInstance as SimpleTaskInstance, TaskInstance as TaskInstance
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.models.tasklog import LogTemplate as LogTemplate
from airflow.models.taskmixin import DAGNode as DAGNode
from airflow.models.xcom_arg import XComArg as XComArg, deserialize_xcom_arg as deserialize_xcom_arg, serialize_xcom_arg as serialize_xcom_arg
from airflow.providers.cncf.kubernetes.pod_generator import PodGenerator as PodGenerator
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.serialization.dag_dependency import DagDependency as DagDependency
from airflow.serialization.enums import Encoding as Encoding
from airflow.serialization.helpers import serialize_template_field as serialize_template_field
from airflow.serialization.json_schema import Validator as Validator, load_dag_schema as load_dag_schema
from airflow.serialization.pydantic.dag import DagModelPydantic as DagModelPydantic
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.serialization.pydantic.dataset import DatasetPydantic as DatasetPydantic
from airflow.serialization.pydantic.job import JobPydantic as JobPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.serialization.pydantic.tasklog import LogTemplatePydantic as LogTemplatePydantic
from airflow.serialization.pydantic.trigger import TriggerPydantic as TriggerPydantic
from airflow.settings import DAGS_FOLDER as DAGS_FOLDER, json as json
from airflow.task.priority_strategy import PriorityWeightStrategy as PriorityWeightStrategy, airflow_priority_weight_strategies as airflow_priority_weight_strategies, airflow_priority_weight_strategies_classes as airflow_priority_weight_strategies_classes
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.timetables.base import Timetable as Timetable
from airflow.triggers.base import BaseTrigger as BaseTrigger, StartTriggerArgs as StartTriggerArgs
from airflow.utils.code_utils import get_python_source as get_python_source
from airflow.utils.context import ConnectionAccessor as ConnectionAccessor, Context as Context, OutletEventAccessor as OutletEventAccessor, OutletEventAccessors as OutletEventAccessors, VariableAccessor as VariableAccessor
from airflow.utils.db import LazySelectSequence as LazySelectSequence
from airflow.utils.docs import get_docs_url as get_docs_url
from airflow.utils.module_loading import import_string as import_string, qualname as qualname
from airflow.utils.operator_resources import Resources as Resources
from airflow.utils.pydantic import BaseModel as BaseModel
from airflow.utils.task_group import MappedTaskGroup as MappedTaskGroup, TaskGroup as TaskGroup
from airflow.utils.timezone import from_timestamp as from_timestamp, parse_timezone as parse_timezone
from airflow.utils.types import ArgNotSet as ArgNotSet, AttributeRemoved as AttributeRemoved, NOTSET as NOTSET
from dateutil import relativedelta
from pendulum.tz.timezone import FixedTimezone, Timezone
from typing import Any, Iterable, NamedTuple

HAS_KUBERNETES: bool
log: Incomplete

def get_operator_extra_links() -> set[str]: ...
def encode_relativedelta(var: relativedelta.relativedelta) -> dict[str, Any]: ...
def decode_relativedelta(var: dict[str, Any]) -> relativedelta.relativedelta: ...
def encode_timezone(var: Timezone | FixedTimezone) -> str | int: ...
def decode_timezone(var: str | int) -> Timezone | FixedTimezone: ...

class _TimetableNotRegistered(ValueError):
    type_string: Incomplete
    def __init__(self, type_string: str) -> None: ...

class _PriorityWeightStrategyNotRegistered(AirflowException):
    type_string: Incomplete
    def __init__(self, type_string: str) -> None: ...

def encode_dataset_condition(var: BaseDataset) -> dict[str, Any]: ...
def decode_dataset_condition(var: dict[str, Any]) -> BaseDataset: ...
def encode_outlet_event_accessor(var: OutletEventAccessor) -> dict[str, Any]: ...
def decode_outlet_event_accessor(var: dict[str, Any]) -> OutletEventAccessor: ...
def encode_timetable(var: Timetable) -> dict[str, Any]: ...
def decode_timetable(var: dict[str, Any]) -> Timetable: ...
def encode_priority_weight_strategy(var: PriorityWeightStrategy) -> str: ...
def decode_priority_weight_strategy(var: str) -> PriorityWeightStrategy: ...
def encode_start_trigger_args(var: StartTriggerArgs) -> dict[str, Any]: ...
def decode_start_trigger_args(var: dict[str, Any]) -> StartTriggerArgs: ...

class _XComRef(NamedTuple):
    data: dict
    def deref(self, dag: DAG) -> XComArg: ...

class _ExpandInputRef(NamedTuple):
    key: str
    value: _ExpandInputSerializedValue
    @classmethod
    def validate_expand_input_value(cls, value: _ExpandInputOriginalValue) -> None: ...
    def deref(self, dag: DAG) -> ExpandInput: ...

def add_pydantic_class_type_mapping(attribute_type: str, orm_class, pydantic_class): ...

class BaseSerialization:
    SERIALIZER_VERSION: int
    @classmethod
    def to_json(cls, var: DAG | BaseOperator | dict | list | set | tuple) -> str: ...
    @classmethod
    def to_dict(cls, var: DAG | BaseOperator | dict | list | set | tuple) -> dict: ...
    @classmethod
    def from_json(cls, serialized_obj: str) -> BaseSerialization | dict | list | set | tuple: ...
    @classmethod
    def from_dict(cls, serialized_obj: dict[Encoding, Any]) -> BaseSerialization | dict | list | set | tuple: ...
    @classmethod
    def validate_schema(cls, serialized_obj: str | dict) -> None: ...
    @classmethod
    def serialize_to_json(cls, object_to_serialize: BaseOperator | MappedOperator | DAG, decorated_fields: set) -> dict[str, Any]: ...
    @classmethod
    def serialize(cls, var: Any, *, strict: bool = False, use_pydantic_models: bool = False) -> Any: ...
    @classmethod
    def default_serialization(cls, strict, var) -> str: ...
    @classmethod
    def deserialize(cls, encoded_var: Any, use_pydantic_models: bool = False) -> Any: ...

class DependencyDetector:
    @staticmethod
    def detect_task_dependencies(task: Operator) -> list[DagDependency]: ...
    @staticmethod
    def detect_dag_dependencies(dag: DAG | None) -> Iterable[DagDependency]: ...

class SerializedBaseOperator(BaseOperator, BaseSerialization):
    ui_color: Incomplete
    ui_fgcolor: Incomplete
    template_ext: Incomplete
    template_fields: Incomplete
    operator_extra_links: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def task_type(self) -> str: ...
    @task_type.setter
    def task_type(self, task_type: str): ...
    @property
    def operator_name(self) -> str: ...
    @operator_name.setter
    def operator_name(self, operator_name: str): ...
    @classmethod
    def serialize_mapped_operator(cls, op: MappedOperator) -> dict[str, Any]: ...
    @classmethod
    def serialize_operator(cls, op: BaseOperator | MappedOperator) -> dict[str, Any]: ...
    @classmethod
    def populate_operator(cls, op: Operator, encoded_op: dict[str, Any]) -> None: ...
    @staticmethod
    def set_task_dag_references(task: Operator, dag: DAG) -> None: ...
    @classmethod
    def deserialize_operator(cls, encoded_op: dict[str, Any]) -> Operator: ...
    @classmethod
    def detect_dependencies(cls, op: Operator) -> set[DagDependency]: ...
    @classmethod
    def serialize(cls, var: Any, *, strict: bool = False, use_pydantic_models: bool = False) -> Any: ...
    @classmethod
    def deserialize(cls, encoded_var: Any, use_pydantic_models: bool = False) -> Any: ...

class SerializedDAG(DAG, BaseSerialization):
    @classmethod
    def serialize_dag(cls, dag: DAG) -> dict: ...
    @classmethod
    def deserialize_dag(cls, encoded_dag: dict[str, Any]) -> SerializedDAG: ...
    @classmethod
    def to_dict(cls, var: Any) -> dict: ...
    @classmethod
    def from_dict(cls, serialized_obj: dict) -> SerializedDAG: ...

class TaskGroupSerialization(BaseSerialization):
    @classmethod
    def serialize_task_group(cls, task_group: TaskGroup) -> dict[str, Any] | None: ...
    @classmethod
    def deserialize_task_group(cls, encoded_group: dict[str, Any], parent_group: TaskGroup | None, task_dict: dict[str, Operator], dag: SerializedDAG) -> TaskGroup: ...
