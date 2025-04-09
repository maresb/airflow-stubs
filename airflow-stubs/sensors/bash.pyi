from _typeshed import Incomplete
from airflow.exceptions import AirflowFailException as AirflowFailException
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.utils.context import Context as Context
from typing import Sequence

class BashSensor(BaseSensorOperator):
    template_fields: Sequence[str]
    bash_command: Incomplete
    env: Incomplete
    output_encoding: Incomplete
    retry_exit_code: Incomplete
    def __init__(self, *, bash_command, env: Incomplete | None = None, output_encoding: str = 'utf-8', retry_exit_code: int | None = None, **kwargs) -> None: ...
    def poke(self, context: Context): ...
