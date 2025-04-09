from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from flask import Flask as Flask

def init_wsgi_middleware(flask_app: Flask) -> None: ...
