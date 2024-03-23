from airflow.models.baseoperator import chain as chain
from airflow.models.dag import DAG as DAG
from airflow.operators.empty import EmptyOperator as EmptyOperator, task_1 as task_1, task_2 as task_2, task_3 as task_3, task_4 as task_4, task_5 as task_5, task_6 as task_6, task_7 as task_7
from airflow.operators.python import ShortCircuitOperator as ShortCircuitOperator, cond_false as cond_false, cond_true as cond_true, short_circuit as short_circuit
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

ds_true: list
ds_false: list
