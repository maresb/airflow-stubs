from airflow.api_connexion import security as security
from airflow.api_connexion.schemas.provider_schema import Provider as Provider, ProviderCollection as ProviderCollection, provider_collection_schema as provider_collection_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import AccessView as AccessView
from airflow.providers_manager import ProviderInfo as ProviderInfo, ProvidersManager as ProvidersManager

def get_providers() -> APIResponse: ...
