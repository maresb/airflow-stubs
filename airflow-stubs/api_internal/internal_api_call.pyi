import typing
import typing_extensions
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException, AirflowException as AirflowException
from typing import Callable, ClassVar

PS: typing_extensions.ParamSpec
RT: typing.TypeVar

class InternalApiConfig:
    _initialized: ClassVar[bool] = ...
    _use_internal_api: ClassVar[bool] = ...
    _internal_api_endpoint: ClassVar[str] = ...
    @staticmethod
    def force_database_direct_access(): ...
    @staticmethod
    def get_use_internal_api(): ...
    @staticmethod
    def get_internal_api_endpoint(): ...
def internal_api_call(func: Callable[PS, RT]) -> Callable[PS, RT]: ...
