import gunicorn.app.base
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.utils.docs import get_docs_url as get_docs_url
from airflow.utils.jwt_signer import JWTSigner as JWTSigner
from airflow.utils.module_loading import import_string as import_string
from typing import NamedTuple

logger: Incomplete

def create_app(): ...

class GunicornOption(NamedTuple):
    key: Incomplete
    value: Incomplete

class StandaloneGunicornApplication(gunicorn.app.base.BaseApplication):
    options: Incomplete
    application: Incomplete
    def __init__(self, app, options: Incomplete | None = None) -> None: ...
    def load_config(self) -> None: ...
    def load(self): ...

def serve_logs(port: Incomplete | None = None): ...
