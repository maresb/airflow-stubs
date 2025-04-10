from airflow.api_connexion.schemas.version_schema import version_info_schema as version_info_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.utils.platform import get_airflow_git_version as get_airflow_git_version
from typing import NamedTuple

class VersionInfo(NamedTuple):
    version: str
    git_version: str | None

def get_version() -> APIResponse: ...
