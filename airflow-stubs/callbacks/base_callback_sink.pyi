from airflow.callbacks.callback_requests import CallbackRequest as CallbackRequest

class BaseCallbackSink:
    def send(self, callback: CallbackRequest) -> None: ...
