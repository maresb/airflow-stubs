import datetime
from airflow.configuration import conf as conf
from typing import ClassVar

class SecretCache:
    class NotPresentException(Exception): ...
    class _CacheValue:
        def __init__(self, value: str | None) -> None: ...
        def is_expired(self, ttl: datetime.timedelta) -> bool: ...
    _SecretCache__manager: ClassVar[None] = ...
    _cache: ClassVar[None] = ...
    _VARIABLE_PREFIX: ClassVar[str] = ...
    _CONNECTION_PREFIX: ClassVar[str] = ...
    @classmethod
    def init(cls): ...
    @classmethod
    def reset(cls): ...
    @classmethod
    def get_variable(cls, key: str) -> str | None: ...
    @classmethod
    def get_connection_uri(cls, conn_id: str) -> str: ...
    @classmethod
    def save_variable(cls, key: str, value: str | None): ...
    @classmethod
    def save_connection_uri(cls, conn_id: str, uri: str): ...
    @classmethod
    def invalidate_variable(cls, key: str): ...
