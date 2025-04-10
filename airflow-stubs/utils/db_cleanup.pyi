from _typeshed import Incomplete
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import Base as Base
from airflow.utils import timezone as timezone
from airflow.utils.db import reflect_tables as reflect_tables
from airflow.utils.helpers import ask_yesno as ask_yesno
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from dataclasses import dataclass
from pendulum import DateTime as DateTime
from sqlalchemy.orm import Query as Query, Session as Session
from sqlalchemy.sql.expression import ClauseElement, Executable
from typing import Any

logger: Incomplete
ARCHIVE_TABLE_PREFIX: str

@dataclass
class _TableConfig:
    table_name: str
    recency_column_name: str
    extra_columns: list[str] | None = ...
    keep_last: bool = ...
    keep_last_filters: Any | None = ...
    keep_last_group_by: Any | None = ...
    recency_column = ...
    orm_model: Base = ...
    def __post_init__(self) -> None: ...
    def __lt__(self, other): ...
    @property
    def readable_config(self): ...

config_list: list[_TableConfig]
config_dict: dict[str, _TableConfig]

class CreateTableAs(Executable, ClauseElement):
    inherit_cache: bool
    name: Incomplete
    query: Incomplete
    def __init__(self, name, query) -> None: ...

def run_cleanup(*, clean_before_timestamp: DateTime, table_names: list[str] | None = None, dry_run: bool = False, verbose: bool = False, confirm: bool = True, skip_archive: bool = False, session: Session = ...): ...
def export_archived_records(export_format, output_path, table_names: Incomplete | None = None, drop_archives: bool = False, needs_confirm: bool = True, session: Session = ...): ...
def drop_archived_tables(table_names, needs_confirm, session) -> None: ...
