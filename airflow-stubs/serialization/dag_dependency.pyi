from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class DagDependency:
    source: str
    target: str
    dependency_type: str
    dependency_id: str | None = ...
    @property
    def node_id(self): ...
