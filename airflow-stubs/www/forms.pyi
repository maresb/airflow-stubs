from _typeshed import Incomplete
from airflow.compat.functools import cache as cache
from airflow.configuration import conf as conf
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.utils.types import DagRunType as DagRunType
from airflow.www.validators import ReadOnly as ReadOnly, ValidConnID as ValidConnID
from airflow.www.widgets import AirflowDateTimePickerROWidget as AirflowDateTimePickerROWidget, AirflowDateTimePickerWidget as AirflowDateTimePickerWidget, BS3TextAreaROWidget as BS3TextAreaROWidget, BS3TextFieldROWidget as BS3TextFieldROWidget
from flask_appbuilder.forms import DynamicForm
from flask_wtf import FlaskForm
from wtforms.fields import Field

class DateTimeWithTimezoneField(Field):
    widget: Incomplete
    format: Incomplete
    data: Incomplete
    def __init__(self, label: Incomplete | None = None, validators: Incomplete | None = None, datetime_format: str = '%Y-%m-%d %H:%M:%S%Z', **kwargs) -> None: ...
    def process_formdata(self, valuelist) -> None: ...

class DateTimeForm(FlaskForm):
    execution_date: Incomplete

class DagRunEditForm(DynamicForm):
    dag_id: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    run_id: Incomplete
    state: Incomplete
    execution_date: Incomplete
    conf: Incomplete
    note: Incomplete
    def populate_obj(self, item) -> None: ...

class TaskInstanceEditForm(DynamicForm):
    dag_id: Incomplete
    task_id: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    state: Incomplete
    execution_date: Incomplete
    note: Incomplete
    def populate_obj(self, item) -> None: ...

def create_connection_form_class() -> type[DynamicForm]: ...
