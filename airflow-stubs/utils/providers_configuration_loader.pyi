from airflow.typing_compat import ParamSpec as ParamSpec
from typing import Callable, TypeVar

PS = ParamSpec('PS')
RT = TypeVar('RT')

def providers_configuration_loaded(func: Callable[PS, RT]) -> Callable[PS, RT]: ...
