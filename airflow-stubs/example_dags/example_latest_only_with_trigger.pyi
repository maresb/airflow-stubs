from airflow.models.dag import DAG as DAG, dag as dag
from airflow.operators.empty import EmptyOperator as EmptyOperator, task1 as task1, task2 as task2, task3 as task3, task4 as task4
from airflow.operators.latest_only import LatestOnlyOperator as LatestOnlyOperator, latest_only as latest_only
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
