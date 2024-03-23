import typing
import typing_extensions
from typing import Callable

PS: typing_extensions.ParamSpec
RT: typing.TypeVar
def providers_configuration_loaded(func: Callable[PS, RT]) -> Callable[PS, RT]: ...
