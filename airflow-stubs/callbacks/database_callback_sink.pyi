import airflow.callbacks.base_callback_sink
from airflow.callbacks.base_callback_sink import BaseCallbackSink as BaseCallbackSink
from airflow.models.db_callback_request import DbCallbackRequest as DbCallbackRequest
from airflow.utils.session import provide_session as provide_session

TYPE_CHECKING: bool
NEW_SESSION: None

class DatabaseCallbackSink(airflow.callbacks.base_callback_sink.BaseCallbackSink):
    def send(self, *args, **kwargs) -> None: ...
