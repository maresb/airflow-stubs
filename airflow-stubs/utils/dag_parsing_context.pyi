from typing import NamedTuple

class AirflowParsingContext(NamedTuple):
    dag_id: str | None
    task_id: str | None

def get_parsing_context() -> AirflowParsingContext: ...
