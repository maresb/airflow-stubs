from airflow.callbacks.base_callback_sink import BaseCallbackSink as BaseCallbackSink
from airflow.callbacks.callback_requests import CallbackRequest as CallbackRequest
from airflow.models.db_callback_request import DbCallbackRequest as DbCallbackRequest
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

class DatabaseCallbackSink(BaseCallbackSink):
    def send(self, callback: CallbackRequest, session: Session = ...) -> None: ...
