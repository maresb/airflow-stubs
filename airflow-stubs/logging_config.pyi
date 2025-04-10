from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.utils.module_loading import import_string as import_string

log: Incomplete

def configure_logging(): ...
def validate_logging_config(logging_config): ...
