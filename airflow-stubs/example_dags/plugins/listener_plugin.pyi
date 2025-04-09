from _typeshed import Incomplete
from airflow.example_dags.plugins import event_listener as event_listener
from airflow.plugins_manager import AirflowPlugin as AirflowPlugin

class MetadataCollectionPlugin(AirflowPlugin):
    name: str
    listeners: Incomplete
