from airflow.models.dag import DAG as DAG, dag as dag
from airflow.operators.bash import BashOperator as BashOperator, also_run_this as also_run_this, run_this as run_this, task as task, this_will_skip as this_will_skip
from airflow.operators.empty import EmptyOperator as EmptyOperator, run_this_last as run_this_last

i: int
