import typing
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

CLIENT_AUTH: None
def init_app(_): ...

T: typing.TypeVar
def requires_authentication(function: T): ...
