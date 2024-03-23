from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator

def subdag(parent_dag_name, child_dag_name, args) -> DAG: ...
