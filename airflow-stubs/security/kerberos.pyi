from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.utils.net import get_hostname as get_hostname
from enum import Enum

NEED_KRB181_WORKAROUND: bool | None
log: Incomplete

class KerberosMode(Enum):
    STANDARD = 'standard'
    ONE_TIME = 'one-time'

def get_kerberos_principle(principal: str | None) -> str: ...
def renew_from_kt(principal: str | None, keytab: str, exit_on_fail: bool = True): ...
def perform_krb181_workaround(principal: str): ...
def detect_conf_var() -> bool: ...
def run(principal: str | None, keytab: str, mode: KerberosMode = ...): ...
