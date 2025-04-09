from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException

class DockerContainerFailedException(AirflowException):
    logs: Incomplete
    def __init__(self, message: str | None = None, logs: list[str | bytes] | None = None) -> None: ...

class DockerContainerFailedSkipException(AirflowSkipException):
    logs: Incomplete
    def __init__(self, message: str | None = None, logs: list[str | bytes] | None = None) -> None: ...
