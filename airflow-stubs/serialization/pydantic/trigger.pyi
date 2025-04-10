import datetime
from _typeshed import Incomplete
from airflow.utils import timezone as timezone
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict
from typing import Any

class TriggerPydantic(BaseModelPydantic):
    id: int | None
    classpath: str
    encrypted_kwargs: str
    created_date: datetime.datetime
    triggerer_id: int | None
    model_config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def kwargs(self) -> dict[str, Any]: ...
    @kwargs.setter
    def kwargs(self, kwargs: dict[str, Any]) -> None: ...
