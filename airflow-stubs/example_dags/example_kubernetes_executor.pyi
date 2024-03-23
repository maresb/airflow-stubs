from airflow.configuration import conf as conf
from airflow.decorators import task as task
from airflow.decorators.base import base_image_override_task as base_image_override_task, non_root_task as non_root_task, other_namespace_task as other_namespace_task, start_task as start_task, task_with_resource_limits as task_with_resource_limits, test_sharedvolume_mount as test_sharedvolume_mount, test_volume_mount as test_volume_mount
from airflow.example_dags.libs.helper import print_stuff as print_stuff
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.xcom_arg import base_image_task as base_image_task, four_task as four_task, other_ns_task as other_ns_task, sidecar_task as sidecar_task, third_task as third_task, volume_task as volume_task

start_task_executor_config: dict
executor_config_volume_mount: dict
executor_config_sidecar: dict
executor_config_non_root: dict
executor_config_other_ns: dict
worker_container_repository: str
worker_container_tag: str
kube_exec_config_special: dict
k8s_tolerations: list
kube_exec_config_resource_limits: dict
