import typing
from airflow.api_connexion.exceptions import PermissionDenied as PermissionDenied
from airflow.api_connexion.security import check_authentication as check_authentication
from airflow.configuration import conf as conf
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.net import get_hostname as get_hostname
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

T: typing.TypeVar
