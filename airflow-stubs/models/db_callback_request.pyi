from _typeshed import Incomplete
from airflow.callbacks.callback_requests import CallbackRequest as CallbackRequest
from airflow.models.base import Base as Base
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON, UtcDateTime as UtcDateTime

class DbCallbackRequest(Base):
    __tablename__: str
    id: Incomplete
    created_at: Incomplete
    priority_weight: Incomplete
    callback_data: Incomplete
    callback_type: Incomplete
    processor_subdir: Incomplete
    def __init__(self, priority_weight: int, callback: CallbackRequest) -> None: ...
    def get_callback_request(self) -> CallbackRequest: ...
