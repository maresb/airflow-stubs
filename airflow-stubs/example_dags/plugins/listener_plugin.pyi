import airflow.example_dags.plugins.event_listener as event_listener
import airflow.plugins_manager
from airflow.plugins_manager import AirflowPlugin as AirflowPlugin
from typing import ClassVar

class MetadataCollectionPlugin(airflow.plugins_manager.AirflowPlugin):
    name: ClassVar[str] = ...
    listeners: ClassVar[list] = ...
