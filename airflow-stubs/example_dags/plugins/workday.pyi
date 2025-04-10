from _typeshed import Incomplete
from airflow.plugins_manager import AirflowPlugin as AirflowPlugin
from airflow.timetables.base import DagRunInfo as DagRunInfo, DataInterval as DataInterval, TimeRestriction as TimeRestriction, Timetable as Timetable
from pendulum import DateTime

log: Incomplete
holiday_calendar: Incomplete

class AfterWorkdayTimetable(Timetable):
    def get_next_workday(self, d: DateTime, incr: int = 1) -> DateTime: ...
    def infer_manual_data_interval(self, run_after: DateTime) -> DataInterval: ...
    def next_dagrun_info(self, *, last_automated_data_interval: DataInterval | None, restriction: TimeRestriction) -> DagRunInfo | None: ...

class WorkdayTimetablePlugin(AirflowPlugin):
    name: str
    timetables: Incomplete
