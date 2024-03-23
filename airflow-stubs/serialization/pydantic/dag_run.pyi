import airflow.utils.pydantic
from airflow.models.dag import PydanticDag as PydanticDag
from airflow.serialization.pydantic.dataset import DatasetEventPydantic as DatasetEventPydantic
from airflow.utils.pydantic import BaseModelPydantic as BaseModelPydantic, ConfigDict as ConfigDict, is_pydantic_2_installed as is_pydantic_2_installed
from airflow.utils.session import provide_session as provide_session
from typing import ClassVar

TYPE_CHECKING: bool
NEW_SESSION: None

class DagRunPydantic(airflow.utils.pydantic.BaseModel):
    model_config: ClassVar[airflow.utils.pydantic.ConfigDict] = ...
    def get_task_instances(self, *args, **kwargs) -> list[TI]: ...
    def get_task_instance(self, *args, **kwargs) -> TI | TaskInstancePydantic | None: ...
    @property
    def logical_date(self): ...
