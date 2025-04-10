from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.typing_compat import Protocol as Protocol

log: Incomplete

class FernetProtocol(Protocol):
    def decrypt(self, b): ...
    def encrypt(self, b): ...

class NullFernet:
    is_encrypted: bool
    def decrypt(self, b): ...
    def encrypt(self, b): ...

def get_fernet(): ...
