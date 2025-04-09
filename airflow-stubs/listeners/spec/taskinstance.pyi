from _typeshed import Incomplete
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm.session import Session as Session

hookspec: Incomplete

def on_task_instance_running(previous_state: TaskInstanceState | None, task_instance: TaskInstance, session: Session | None): ...
def on_task_instance_success(previous_state: TaskInstanceState | None, task_instance: TaskInstance, session: Session | None): ...
def on_task_instance_failed(previous_state: TaskInstanceState | None, task_instance: TaskInstance, error: None | str | BaseException, session: Session | None): ...
