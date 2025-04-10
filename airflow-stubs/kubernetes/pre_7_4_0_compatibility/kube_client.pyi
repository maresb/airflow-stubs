from _typeshed import Incomplete
from airflow.configuration import conf as conf
from kubernetes import client

log: Incomplete
has_kubernetes: bool
ApiException = BaseException

def get_kube_client(in_cluster: bool = ..., cluster_context: str | None = None, config_file: str | None = None) -> client.CoreV1Api: ...
