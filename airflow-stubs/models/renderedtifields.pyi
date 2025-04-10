from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.models import Operator as Operator
from airflow.models.base import StringID as StringID, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.models.taskinstance import TaskInstance as TaskInstance, TaskInstancePydantic as TaskInstancePydantic
from airflow.serialization.helpers import serialize_template_field as serialize_template_field
from airflow.settings import json as json
from airflow.utils.retries import retry_db_transaction as retry_db_transaction
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session
from sqlalchemy.sql import FromClause as FromClause

def get_serialized_template_fields(task: Operator): ...

class RenderedTaskInstanceFields(TaskInstanceDependencies):
    __tablename__: str
    dag_id: Incomplete
    task_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    rendered_fields: Incomplete
    k8s_pod_yaml: Incomplete
    __table_args__: Incomplete
    task_instance: Incomplete
    dag_run: Incomplete
    execution_date: Incomplete
    ti: Incomplete
    task: Incomplete
    def __init__(self, ti: TaskInstance, render_templates: bool = True, rendered_fields: Incomplete | None = None) -> None: ...
    @classmethod
    def get_templated_fields(cls, ti: TaskInstance | TaskInstancePydantic, session: Session = ...) -> dict | None: ...
    @classmethod
    def get_k8s_pod_yaml(cls, ti: TaskInstance, session: Session = ...) -> dict | None: ...
    def write(self, session: Session = None): ...
    @classmethod
    def delete_old_records(cls, task_id: str, dag_id: str, num_to_keep: int = ..., session: Session = ...) -> None: ...
