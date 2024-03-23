import airflow as airflow
from airflow.www.extensions.init_appbuilder import init_appbuilder as init_appbuilder
from airflow.www.extensions.init_views import init_plugins as init_plugins
from typing import Generator

TYPE_CHECKING: bool
def get_application_builder(*args, **kwds) -> Generator[AirflowAppBuilder, None, None]: ...
