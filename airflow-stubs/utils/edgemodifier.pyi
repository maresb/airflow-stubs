from _typeshed import Incomplete
from airflow.models.taskmixin import DAGNode as DAGNode, DependencyMixin as DependencyMixin
from airflow.utils.task_group import TaskGroup as TaskGroup
from typing import Sequence

class EdgeModifier(DependencyMixin):
    label: Incomplete
    def __init__(self, label: str | None = None) -> None: ...
    @property
    def roots(self): ...
    @property
    def leaves(self): ...
    def set_upstream(self, other: DependencyMixin | Sequence[DependencyMixin], edge_modifier: EdgeModifier | None = None): ...
    def set_downstream(self, other: DependencyMixin | Sequence[DependencyMixin], edge_modifier: EdgeModifier | None = None): ...
    def update_relative(self, other: DependencyMixin, upstream: bool = True, edge_modifier: EdgeModifier | None = None) -> None: ...
    def add_edge_info(self, dag, upstream_id: str, downstream_id: str): ...

def Label(label: str): ...
