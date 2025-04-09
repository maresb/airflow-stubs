from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import ensure_secrets_loaded as ensure_secrets_loaded
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.models.crypto import get_fernet as get_fernet
from airflow.secrets.cache import SecretCache as SecretCache
from airflow.secrets.metastore import MetastoreBackend as MetastoreBackend
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.log.secrets_masker import mask_secret as mask_secret
from airflow.utils.session import provide_session as provide_session
from sqlalchemy.orm import Session as Session
from typing import Any

log: Incomplete

class Variable(Base, LoggingMixin):
    __tablename__: str
    id: Incomplete
    key: Incomplete
    description: Incomplete
    is_encrypted: Incomplete
    def __init__(self, key: Incomplete | None = None, val: Incomplete | None = None, description: Incomplete | None = None) -> None: ...
    def on_db_load(self) -> None: ...
    def get_val(self): ...
    def set_val(self, value) -> None: ...
    def val(cls): ...
    @classmethod
    def setdefault(cls, key, default, description: Incomplete | None = None, deserialize_json: bool = False): ...
    @classmethod
    def get(cls, key: str, default_var: Any = ..., deserialize_json: bool = False) -> Any: ...
    @staticmethod
    def set(key: str, value: Any, description: str | None = None, serialize_json: bool = False, session: Session = None) -> None: ...
    @staticmethod
    def update(key: str, value: Any, serialize_json: bool = False, session: Session = None) -> None: ...
    @staticmethod
    def delete(key: str, session: Session = None) -> int: ...
    def rotate_fernet_key(self) -> None: ...
    @staticmethod
    def check_for_write_conflict(key: str) -> None: ...
    @staticmethod
    def get_variable_from_secrets(key: str) -> str | None: ...
