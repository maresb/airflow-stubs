import airflow.callbacks.base_callback_sink
from airflow.callbacks.base_callback_sink import BaseCallbackSink as BaseCallbackSink
from typing import Callable

TYPE_CHECKING: bool

class PipeCallbackSink(airflow.callbacks.base_callback_sink.BaseCallbackSink):
    def __init__(self, get_sink_pipe: Callable[[], MultiprocessingConnection]) -> None: ...
    def send(self, callback: CallbackRequest): ...
