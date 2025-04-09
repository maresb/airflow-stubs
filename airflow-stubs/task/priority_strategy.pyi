import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.taskinstance import TaskInstance as TaskInstance
from typing import Any

class PriorityWeightStrategy(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_weight(self, ti: TaskInstance): ...
    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> PriorityWeightStrategy: ...
    def serialize(self) -> dict[str, Any]: ...
    def __eq__(self, other: object) -> bool: ...

class _AbsolutePriorityWeightStrategy(PriorityWeightStrategy):
    def get_weight(self, ti: TaskInstance): ...

class _DownstreamPriorityWeightStrategy(PriorityWeightStrategy):
    def get_weight(self, ti: TaskInstance) -> int: ...

class _UpstreamPriorityWeightStrategy(PriorityWeightStrategy):
    def get_weight(self, ti: TaskInstance): ...

airflow_priority_weight_strategies: dict[str, type[PriorityWeightStrategy]]
airflow_priority_weight_strategies_classes: Incomplete

def validate_and_load_priority_weight_strategy(priority_weight_strategy: str | PriorityWeightStrategy | None) -> PriorityWeightStrategy: ...
