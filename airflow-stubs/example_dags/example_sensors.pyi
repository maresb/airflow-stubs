from airflow.models.dag import DAG as DAG, dag as dag
from airflow.operators.bash import BashOperator as BashOperator, t5 as t5, t7 as t7, tx as tx
from airflow.sensors.bash import BashSensor as BashSensor, t3 as t3, t4 as t4
from airflow.sensors.filesystem import FileSensor as FileSensor, t6 as t6
from airflow.sensors.python import PythonSensor as PythonSensor, t8 as t8, t9 as t9
from airflow.sensors.time_delta import TimeDeltaSensor as TimeDeltaSensor, TimeDeltaSensorAsync as TimeDeltaSensorAsync, t0 as t0, t0a as t0a
from airflow.sensors.time_sensor import TimeSensor as TimeSensor, TimeSensorAsync as TimeSensorAsync, t1 as t1, t1a as t1a, t2 as t2, t2a as t2a
from airflow.sensors.weekday import DayOfWeekSensor as DayOfWeekSensor, t10 as t10
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.weekday import WeekDay as WeekDay

def success_callable(): ...
def failure_callable(): ...
