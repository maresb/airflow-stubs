import os
from _typeshed import Incomplete
from abc import ABCMeta
from airflow.compat.functools import cache as cache
from airflow.exceptions import AirflowConfigException as AirflowConfigException, AirflowException as AirflowException, AirflowSkipException as AirflowSkipException, DeserializingResultError as DeserializingResultError, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.skipmixin import SkipMixin as SkipMixin
from airflow.models.variable import Variable as Variable
from airflow.operators.branch import BranchMixIn as BranchMixIn
from airflow.typing_compat import Literal as Literal
from airflow.utils import hashlib_wrapper as hashlib_wrapper
from airflow.utils.context import Context as Context, context_copy_partial as context_copy_partial, context_get_outlet_events as context_get_outlet_events, context_merge as context_merge
from airflow.utils.file import get_unique_dag_module_name as get_unique_dag_module_name
from airflow.utils.operator_helpers import ExecutionCallableRunner as ExecutionCallableRunner, KeywordParameters as KeywordParameters
from airflow.utils.process_utils import execute_in_subprocess as execute_in_subprocess
from airflow.utils.python_virtualenv import prepare_virtualenv as prepare_virtualenv, write_python_script as write_python_script
from collections.abc import Container
from pendulum.datetime import DateTime as DateTime
from typing import Any, Callable, Collection, Iterable, Mapping, NamedTuple, Sequence

log: Incomplete

def is_venv_installed() -> bool: ...
def task(python_callable: Callable | None = None, multiple_outputs: bool | None = None, **kwargs): ...

class _PythonVersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int
    @classmethod
    def from_executable(cls, executable: str) -> _PythonVersionInfo: ...

class PythonOperator(BaseOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    BLUE: str
    ui_color = BLUE
    shallow_copy_attrs: Sequence[str]
    python_callable: Incomplete
    op_args: Incomplete
    op_kwargs: Incomplete
    templates_dict: Incomplete
    template_ext: Incomplete
    show_return_value_in_logs: Incomplete
    def __init__(self, *, python_callable: Callable, op_args: Collection[Any] | None = None, op_kwargs: Mapping[str, Any] | None = None, templates_dict: dict[str, Any] | None = None, templates_exts: Sequence[str] | None = None, show_return_value_in_logs: bool = True, **kwargs) -> None: ...
    def execute(self, context: Context) -> Any: ...
    def determine_kwargs(self, context: Mapping[str, Any]) -> Mapping[str, Any]: ...
    def execute_callable(self) -> Any: ...

class BranchPythonOperator(PythonOperator, BranchMixIn):
    def execute(self, context: Context) -> Any: ...

class ShortCircuitOperator(PythonOperator, SkipMixin):
    ignore_downstream_trigger_rules: Incomplete
    def __init__(self, *, ignore_downstream_trigger_rules: bool = True, **kwargs) -> None: ...
    def execute(self, context: Context) -> Any: ...

class _BasePythonVirtualenvOperator(PythonOperator, metaclass=ABCMeta):
    BASE_SERIALIZABLE_CONTEXT_KEYS: Incomplete
    PENDULUM_SERIALIZABLE_CONTEXT_KEYS: Incomplete
    AIRFLOW_SERIALIZABLE_CONTEXT_KEYS: Incomplete
    string_args: Incomplete
    pickling_library: Incomplete
    serializer: _SerializerTypeDef
    expect_airflow: Incomplete
    skip_on_exit_code: Incomplete
    env_vars: Incomplete
    inherit_env: Incomplete
    def __init__(self, *, python_callable: Callable, serializer: _SerializerTypeDef | None = None, op_args: Collection[Any] | None = None, op_kwargs: Mapping[str, Any] | None = None, string_args: Iterable[str] | None = None, templates_dict: dict | None = None, templates_exts: list[str] | None = None, expect_airflow: bool = True, skip_on_exit_code: int | Container[int] | None = None, env_vars: dict[str, str] | None = None, inherit_env: bool = True, use_dill: bool = False, **kwargs) -> None: ...
    def execute(self, context: Context) -> Any: ...
    def get_python_source(self): ...
    def __deepcopy__(self, memo): ...
    def determine_kwargs(self, context: Mapping[str, Any]) -> Mapping[str, Any]: ...

class PythonVirtualenvOperator(_BasePythonVirtualenvOperator):
    template_fields: Sequence[str]
    template_ext: Sequence[str]
    requirements: list[str]
    python_version: Incomplete
    system_site_packages: Incomplete
    pip_install_options: Incomplete
    index_urls: list[str] | None
    venv_cache_path: Incomplete
    def __init__(self, *, python_callable: Callable, requirements: None | Iterable[str] | str = None, python_version: str | None = None, serializer: _SerializerTypeDef | None = None, system_site_packages: bool = True, pip_install_options: list[str] | None = None, op_args: Collection[Any] | None = None, op_kwargs: Mapping[str, Any] | None = None, string_args: Iterable[str] | None = None, templates_dict: dict | None = None, templates_exts: list[str] | None = None, expect_airflow: bool = True, skip_on_exit_code: int | Container[int] | None = None, index_urls: None | Collection[str] | str = None, venv_cache_path: None | os.PathLike[str] = None, env_vars: dict[str, str] | None = None, inherit_env: bool = True, use_dill: bool = False, **kwargs) -> None: ...
    def execute_callable(self): ...

class BranchPythonVirtualenvOperator(PythonVirtualenvOperator, BranchMixIn):
    def execute(self, context: Context) -> Any: ...

class ExternalPythonOperator(_BasePythonVirtualenvOperator):
    template_fields: Sequence[str]
    python: Incomplete
    expect_pendulum: Incomplete
    def __init__(self, *, python: str, python_callable: Callable, serializer: _SerializerTypeDef | None = None, op_args: Collection[Any] | None = None, op_kwargs: Mapping[str, Any] | None = None, string_args: Iterable[str] | None = None, templates_dict: dict | None = None, templates_exts: list[str] | None = None, expect_airflow: bool = True, expect_pendulum: bool = False, skip_on_exit_code: int | Container[int] | None = None, env_vars: dict[str, str] | None = None, inherit_env: bool = True, use_dill: bool = False, **kwargs) -> None: ...
    def execute_callable(self): ...

class BranchExternalPythonOperator(ExternalPythonOperator, BranchMixIn):
    def execute(self, context: Context) -> Any: ...

def get_current_context() -> Context: ...
