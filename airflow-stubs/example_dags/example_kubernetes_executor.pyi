from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.decorators import task as task
from airflow.example_dags.libs.helper import print_stuff as print_stuff
from airflow.models.dag import DAG as DAG

log: Incomplete
start_task_executor_config: Incomplete

def start_task() -> None: ...

executor_config_volume_mount: Incomplete

def test_volume_mount() -> None: ...

volume_task: Incomplete
executor_config_sidecar: Incomplete

def test_sharedvolume_mount() -> None: ...

sidecar_task: Incomplete
executor_config_non_root: Incomplete

def non_root_task() -> None: ...

third_task: Incomplete
executor_config_other_ns: Incomplete

def other_namespace_task() -> None: ...

other_ns_task: Incomplete
worker_container_repository: Incomplete
worker_container_tag: Incomplete
kube_exec_config_special: Incomplete

def base_image_override_task() -> None: ...

base_image_task: Incomplete
k8s_affinity: Incomplete
k8s_tolerations: Incomplete
k8s_resource_requirements: Incomplete
kube_exec_config_resource_limits: Incomplete

def task_with_resource_limits() -> None: ...

four_task: Incomplete
