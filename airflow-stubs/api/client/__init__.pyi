import airflow.api as api
from airflow.configuration import conf as conf

TYPE_CHECKING: bool
def get_current_api_client() -> Client: ...
