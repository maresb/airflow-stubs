from typing import Any, Callable, TypeVar

CLIENT_AUTH: tuple[str, str] | Any | None

def init_app(_) -> None: ...
T = TypeVar('T', bound=Callable)

def requires_authentication(function: T): ...
