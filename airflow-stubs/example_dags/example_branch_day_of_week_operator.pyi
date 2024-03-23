from airflow.models.dag import DAG as DAG, dag as dag
from airflow.operators.empty import EmptyOperator as EmptyOperator, empty_task_1 as empty_task_1, empty_task_2 as empty_task_2, empty_task_3 as empty_task_3, empty_task_4 as empty_task_4
from airflow.operators.weekday import BranchDayOfWeekOperator as BranchDayOfWeekOperator, branch as branch, branch_weekend as branch_weekend
from airflow.utils.weekday import WeekDay as WeekDay
