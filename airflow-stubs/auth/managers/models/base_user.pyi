class BaseUser:
    def get_id(self) -> str: ...
    def get_name(self) -> str: ...
    @property
    def is_active(self): ...
