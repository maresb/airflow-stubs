import airflow.utils.pydantic
from airflow.utils.pydantic import BaseModelPydantic as BaseModelPydantic, ConfigDict as ConfigDict
from typing import ClassVar

class DagScheduleDatasetReferencePydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...

class TaskOutletDatasetReferencePydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...

class DatasetPydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...

class DatasetEventPydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...
