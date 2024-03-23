from airflow.models.dag import DAG as DAG, dag as dag
from airflow.operators.empty import EmptyOperator as EmptyOperator, task1 as task1
from airflow.operators.latest_only import LatestOnlyOperator as LatestOnlyOperator, latest_only as latest_only
