import airflow.utils.pydantic
from airflow.utils.pydantic import BaseModelPydantic as BaseModelPydantic, ConfigDict as ConfigDict
from typing import ClassVar

class LogTemplatePydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...
