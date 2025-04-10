from _typeshed import Incomplete
from airflow.utils.hashlib_wrapper import md5 as md5
from kubernetes.client import models as k8s

MAX_POD_ID_LEN: int
MAX_LABEL_LEN: int

class PodDefaults:
    XCOM_MOUNT_PATH: str
    SIDECAR_CONTAINER_NAME: str
    XCOM_CMD: str
    VOLUME_MOUNT: Incomplete
    VOLUME: Incomplete
    SIDECAR_CONTAINER: Incomplete

def make_safe_label_value(string): ...

class PodGenerator:
    pod: Incomplete
    metadata: Incomplete
    container: Incomplete
    spec: Incomplete
    extract_xcom: Incomplete
    def __init__(self, image: str | None = None, name: str | None = None, namespace: str | None = None, volume_mounts: list[k8s.V1VolumeMount | dict] | None = None, envs: dict[str, str] | None = None, cmds: list[str] | None = None, args: list[str] | None = None, labels: dict[str, str] | None = None, node_selectors: dict[str, str] | None = None, ports: list[k8s.V1ContainerPort | dict] | None = None, volumes: list[k8s.V1Volume | dict] | None = None, image_pull_policy: str | None = None, restart_policy: str | None = None, image_pull_secrets: str | None = None, init_containers: list[k8s.V1Container] | None = None, service_account_name: str | None = None, resources: k8s.V1ResourceRequirements | dict | None = None, annotations: dict[str, str] | None = None, affinity: dict | None = None, hostnetwork: bool = False, tolerations: list | None = None, security_context: k8s.V1PodSecurityContext | dict | None = None, configmaps: list[str] | None = None, dnspolicy: str | None = None, schedulername: str | None = None, extract_xcom: bool = False, priority_class_name: str | None = None) -> None: ...
    def gen_pod(self) -> k8s.V1Pod: ...
    @staticmethod
    def add_sidecar(pod: k8s.V1Pod) -> k8s.V1Pod: ...
    @staticmethod
    def from_obj(obj) -> k8s.V1Pod | None: ...
    @staticmethod
    def make_unique_pod_id(dag_id): ...
