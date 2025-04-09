from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.www.session import AirflowDatabaseSessionInterface as AirflowDatabaseSessionInterface, AirflowSecureCookieSessionInterface as AirflowSecureCookieSessionInterface

def init_airflow_session_interface(app) -> None: ...
