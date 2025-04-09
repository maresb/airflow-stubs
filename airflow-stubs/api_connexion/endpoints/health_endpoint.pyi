from airflow.api.common.airflow_health import get_airflow_health as get_airflow_health
from airflow.api_connexion.schemas.health_schema import health_schema as health_schema
from airflow.api_connexion.types import APIResponse as APIResponse

def get_health() -> APIResponse: ...
