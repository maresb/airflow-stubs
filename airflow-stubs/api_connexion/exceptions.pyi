import connexion.exceptions
import flask
from airflow.utils.docs import get_docs_url as get_docs_url
from typing import Any

TYPE_CHECKING: bool
doc_link: str
EXCEPTIONS_LINK_MAP: dict
def common_error_handler(exception: BaseException) -> flask.Response: ...

class NotFound(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...

class BadRequest(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...

class Unauthenticated(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...

class PermissionDenied(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...

class AlreadyExists(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...

class Unknown(connexion.exceptions.ProblemException):
    def __init__(self, title: str = ..., detail: str | None = ..., headers: dict | None = ..., **kwargs: Any) -> None: ...
