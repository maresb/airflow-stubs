import airflow.api_connexion.security as security
from airflow.api_connexion.schemas.provider_schema import Provider as Provider, ProviderCollection as ProviderCollection, provider_collection_schema as provider_collection_schema
from airflow.auth.managers.models.resource_details import AccessView as AccessView
from airflow.providers_manager import ProvidersManager as ProvidersManager

TYPE_CHECKING: bool
def get_providers(*args, **kwargs) -> APIResponse: ...
