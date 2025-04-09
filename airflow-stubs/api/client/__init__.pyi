from airflow import api as api
from airflow.api.client.api_client import Client as Client
from airflow.configuration import conf as conf

def get_current_api_client() -> Client: ...
