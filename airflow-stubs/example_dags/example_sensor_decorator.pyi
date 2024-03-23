from airflow.decorators import task as task
from airflow.models.dag import dag as dag, tutorial_etl_dag as tutorial_etl_dag
from airflow.sensors.base import PokeReturnValue as PokeReturnValue

def example_sensor_decorator(*args, **kwargs): ...
