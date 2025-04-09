from _typeshed import Incomplete
from airflow.models.dag import DAG as DAG
from airflow.operators.bash import BashOperator as BashOperator
from airflow.sensors.bash import BashSensor as BashSensor
from airflow.sensors.filesystem import FileSensor as FileSensor
from airflow.sensors.python import PythonSensor as PythonSensor
from airflow.sensors.time_delta import TimeDeltaSensor as TimeDeltaSensor, TimeDeltaSensorAsync as TimeDeltaSensorAsync
from airflow.sensors.time_sensor import TimeSensor as TimeSensor, TimeSensorAsync as TimeSensorAsync
from airflow.sensors.weekday import DayOfWeekSensor as DayOfWeekSensor
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.weekday import WeekDay as WeekDay

def success_callable(): ...
def failure_callable(): ...

t0: Incomplete
t0a: Incomplete
t1: Incomplete
t2: Incomplete
t1a: Incomplete
t2a: Incomplete
t3: Incomplete
t4: Incomplete
t5: Incomplete
t6: Incomplete
t7: Incomplete
t8: Incomplete
t9: Incomplete
t10: Incomplete
t11: Incomplete
tx: Incomplete
