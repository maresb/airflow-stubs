from airflow.decorators.base import TaskDecorator as TaskDecorator, get_unique_task_id as get_unique_task_id, task_decorator_factory as task_decorator_factory
from airflow.sensors.python import PythonSensor as PythonSensor
from typing import Callable, Sequence

class DecoratedSensorOperator(PythonSensor):
    template_fields: Sequence[str]
    template_fields_renderers: dict[str, str]
    custom_operator_name: str
    shallow_copy_attrs: Sequence[str]
    def __init__(self, *, task_id: str, **kwargs) -> None: ...

def sensor_task(python_callable: Callable | None = None, **kwargs) -> TaskDecorator: ...
