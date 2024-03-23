import client
from airflow.configuration import conf as conf

has_kubernetes: bool
def get_kube_client(in_cluster: bool = ..., cluster_context: str | None = ..., config_file: str | None = ...) -> client.CoreV1Api: ...
