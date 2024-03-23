from airflow.decorators import task as task
from airflow.models.baseoperator import chain as chain
from airflow.models.dag import dag as dag, example_dag as example_dag
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

def example_short_circuit_decorator(*args, **kwargs): ...
