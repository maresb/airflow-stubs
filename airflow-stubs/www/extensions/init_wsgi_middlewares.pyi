from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException

TYPE_CHECKING: bool
def init_wsgi_middleware(flask_app: Flask) -> None: ...
