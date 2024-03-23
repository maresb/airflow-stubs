from airflow.models.dag import DAG as DAG, child_dag as child_dag, parent_dag as parent_dag
from airflow.operators.empty import EmptyOperator as EmptyOperator, child_task3 as child_task3
from airflow.sensors.external_task import ExternalTaskMarker as ExternalTaskMarker, ExternalTaskSensor as ExternalTaskSensor, child_task1 as child_task1, child_task2 as child_task2, parent_task as parent_task
