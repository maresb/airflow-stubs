import abc
from abc import ABC, abstractmethod
from kubernetes.client import models as k8s

class K8SModel(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def attach_to_pod(self, pod: k8s.V1Pod) -> k8s.V1Pod: ...

def append_to_pod(pod: k8s.V1Pod, k8s_objects: list[K8SModel] | None): ...
