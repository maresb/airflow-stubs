import airflow as airflow
from airflow.configuration import conf as conf
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import get_airflow_git_version as get_airflow_git_version
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

IS_K8S_OR_K8SCELERY_EXECUTOR: bool
STATE_COLORS: dict
def init_jinja_globals(app): ...
