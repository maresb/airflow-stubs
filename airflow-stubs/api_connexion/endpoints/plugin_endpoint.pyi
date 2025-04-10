from airflow.api_connexion import security as security
from airflow.api_connexion.parameters import check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.plugin_schema import PluginCollection as PluginCollection, plugin_collection_schema as plugin_collection_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import AccessView as AccessView
from airflow.plugins_manager import get_plugin_info as get_plugin_info

def get_plugins(*, limit: int, offset: int = 0) -> APIResponse: ...
