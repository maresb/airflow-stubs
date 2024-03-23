import httpx
from _typeshed import Incomplete

class Client:
    def __init__(self, api_base_url, auth: Incomplete | None = ..., session: httpx.Client | None = ...) -> None: ...
    def trigger_dag(self, dag_id, run_id: Incomplete | None = ..., conf: Incomplete | None = ..., execution_date: Incomplete | None = ..., replace_microseconds: bool = ...): ...
    def delete_dag(self, dag_id): ...
    def get_pool(self, name): ...
    def get_pools(self): ...
    def create_pool(self, name, slots, description, include_deferred): ...
    def delete_pool(self, name): ...
    def get_lineage(self, dag_id: str, execution_date: str): ...