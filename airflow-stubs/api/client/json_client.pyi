import airflow.api.client.api_client
import airflow.api.client.api_client as api_client
from _typeshed import Incomplete

class Client(airflow.api.client.api_client.Client):
    def trigger_dag(self, dag_id, run_id: Incomplete | None = ..., conf: Incomplete | None = ..., execution_date: Incomplete | None = ..., replace_microseconds: bool = ...): ...
    def delete_dag(self, dag_id: str): ...
    def get_pool(self, name: str): ...
    def get_pools(self): ...
    def create_pool(self, name: str, slots: int, description: str, include_deferred: bool): ...
    def delete_pool(self, name: str): ...
    def get_lineage(self, dag_id: str, execution_date: str): ...
