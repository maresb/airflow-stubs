from airflow.models.dagbag import DagBag as DagBag
from airflow.www.extensions.init_appbuilder import AirflowAppBuilder as AirflowAppBuilder
from flask import Flask
from typing import Any

class AirflowApp(Flask):
    appbuilder: AirflowAppBuilder
    dag_bag: DagBag
    api_auth: list[Any]

def get_airflow_app() -> AirflowApp: ...
