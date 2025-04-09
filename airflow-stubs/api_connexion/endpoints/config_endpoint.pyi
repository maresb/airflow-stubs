from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import NotFound as NotFound, PermissionDenied as PermissionDenied
from airflow.api_connexion.schemas.config_schema import Config as Config, ConfigOption as ConfigOption, ConfigSection as ConfigSection, config_schema as config_schema
from airflow.configuration import conf as conf
from airflow.settings import json as json
from flask import Response

LINE_SEP: str

def get_config(*, section: str | None = None) -> Response: ...
def get_value(*, section: str, option: str) -> Response: ...
