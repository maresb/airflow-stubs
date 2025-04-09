from _typeshed import Incomplete
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict
from datetime import datetime

class LogTemplatePydantic(BaseModelPydantic):
    id: int
    filename: str
    elasticsearch_id: str
    created_at: datetime
    model_config: Incomplete
