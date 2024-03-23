import airflow.utils.cli as cli_utils
from airflow.models.connection import Connection as Connection
from airflow.models.variable import Variable as Variable
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.session import create_session as create_session

def rotate_fernet_key(*args, **kwargs): ...
