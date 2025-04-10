from airflow.callbacks.base_callback_sink import BaseCallbackSink as BaseCallbackSink
from airflow.callbacks.callback_requests import CallbackRequest as CallbackRequest
from multiprocessing.connection import Connection as MultiprocessingConnection
from typing import Callable

class PipeCallbackSink(BaseCallbackSink):
    def __init__(self, get_sink_pipe: Callable[[], MultiprocessingConnection]) -> None: ...
    def send(self, callback: CallbackRequest): ...
