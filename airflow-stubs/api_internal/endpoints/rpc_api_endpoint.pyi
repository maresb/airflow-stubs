from _typeshed import Incomplete
from airflow.api_connexion.exceptions import PermissionDenied as PermissionDenied
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.jobs.job import Job as Job, most_recent_job as most_recent_job
from airflow.models.dagcode import DagCode as DagCode
from airflow.serialization.serialized_objects import BaseSerialization as BaseSerialization
from airflow.utils.jwt_signer import JWTSigner as JWTSigner
from airflow.utils.session import create_session as create_session
from typing import Any, Callable

log: Incomplete

def initialize_method_map() -> dict[str, Callable]: ...
def log_and_build_error_response(message, status): ...
def internal_airflow_api(body: dict[str, Any]) -> APIResponse: ...
