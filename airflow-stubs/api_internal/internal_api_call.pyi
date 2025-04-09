from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException, AirflowException as AirflowException
from airflow.settings import force_traceback_session_for_untrusted_components as force_traceback_session_for_untrusted_components
from airflow.typing_compat import ParamSpec as ParamSpec
from airflow.utils.jwt_signer import JWTSigner as JWTSigner
from http import HTTPStatus
from typing import Callable, TypeVar

PS = ParamSpec('PS')
RT = TypeVar('RT')
logger: Incomplete

class AirflowHttpException(AirflowException):
    status_code: Incomplete
    def __init__(self, message: str, status_code: HTTPStatus) -> None: ...

class InternalApiConfig:
    @staticmethod
    def set_use_database_access(component: str): ...
    @staticmethod
    def set_use_internal_api(component: str, allow_tests_to_use_db: bool = False): ...
    @staticmethod
    def get_use_internal_api(): ...
    @staticmethod
    def get_internal_api_endpoint(): ...

def internal_api_call(func: Callable[PS, RT]) -> Callable[PS, RT]: ...
