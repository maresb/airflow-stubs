from airflow.models import Operator as Operator
from airflow.models.abstractoperator import AbstractOperator as AbstractOperator
from airflow.models.dag import DAG as DAG

def dag_edges(dag: DAG): ...
