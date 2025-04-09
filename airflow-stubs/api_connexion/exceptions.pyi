import flask
from _typeshed import Incomplete
from airflow.utils.docs import get_docs_url as get_docs_url
from connexion import ProblemException
from typing import Any

doc_link: Incomplete
EXCEPTIONS_LINK_MAP: Incomplete

def common_error_handler(exception: BaseException) -> flask.Response: ...

class NotFound(ProblemException):
    def __init__(self, title: str = 'Not Found', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...

class BadRequest(ProblemException):
    def __init__(self, title: str = 'Bad Request', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...

class Unauthenticated(ProblemException):
    def __init__(self, title: str = 'Unauthorized', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...

class PermissionDenied(ProblemException):
    def __init__(self, title: str = 'Forbidden', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...

class AlreadyExists(ProblemException):
    def __init__(self, title: str = 'Conflict', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...

class Unknown(ProblemException):
    def __init__(self, title: str = 'Internal Server Error', detail: str | None = None, headers: dict | None = None, **kwargs: Any) -> None: ...
