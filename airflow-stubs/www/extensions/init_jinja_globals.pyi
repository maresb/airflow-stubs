from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.settings import IS_K8S_OR_K8SCELERY_EXECUTOR as IS_K8S_OR_K8SCELERY_EXECUTOR, STATE_COLORS as STATE_COLORS
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import get_airflow_git_version as get_airflow_git_version
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

logger: Incomplete

def init_jinja_globals(app): ...
