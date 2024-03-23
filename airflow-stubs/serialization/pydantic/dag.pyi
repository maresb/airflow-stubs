import airflow.settings as settings
import airflow.utils.pydantic
from airflow.configuration import airflow_conf as airflow_conf
from airflow.models.dag import DAG as DAG, PydanticDag as PydanticDag
from airflow.utils.pydantic import BaseModelPydantic as BaseModelPydantic, ConfigDict as ConfigDict, PlainSerializer as PlainSerializer, PlainValidator as PlainValidator, ValidationInfo as ValidationInfo
from airflow.utils.sqlalchemy import Interval as Interval, PydanticInterval as PydanticInterval
from typing import Any, ClassVar

def serialize_interval(value: Interval) -> Interval: ...
def validate_interval(value: Interval | Any, _info: ValidationInfo) -> Any: ...
def serialize_operator(x: DAG) -> dict: ...
def validate_operator(x: DAG | dict[str, Any], _info: ValidationInfo) -> Any: ...

class DagOwnerAttributesPydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...

class DagTagPydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...

class DagModelPydantic(airflow.utils.pydantic.BaseModel):
    is_paused_at_creation: ClassVar[bool] = ...
    is_paused: ClassVar[bool] = ...
    is_subdag: ClassVar[bool] = ...
    is_active: ClassVar[bool] = ...
    has_import_errors: ClassVar[bool] = ...
    _processor_dags_folder: ClassVar[None] = ...
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...
    @property
    def relative_fileloc(self): ...
