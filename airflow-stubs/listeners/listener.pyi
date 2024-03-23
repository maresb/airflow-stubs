from airflow.plugins_manager import integrate_listener_plugins as integrate_listener_plugins

TYPE_CHECKING: bool

class ListenerManager:
    def __init__(self) -> None: ...
    def add_listener(self, listener): ...
    def clear(self): ...
    @property
    def has_listeners(self): ...
    @property
    def hook(self): ...
def get_listener_manager() -> ListenerManager: ...
