TYPE_CHECKING: bool

class BaseCallbackSink:
    def send(self, callback: CallbackRequest) -> None: ...
