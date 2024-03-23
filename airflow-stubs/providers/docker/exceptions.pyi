import airflow.exceptions
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException

class DockerContainerFailedException(airflow.exceptions.AirflowException):
    def __init__(self, message: str | None = ..., logs: list[str | bytes] | None = ...) -> None: ...

class DockerContainerFailedSkipException(airflow.exceptions.AirflowSkipException):
    def __init__(self, message: str | None = ..., logs: list[str | bytes] | None = ...) -> None: ...
