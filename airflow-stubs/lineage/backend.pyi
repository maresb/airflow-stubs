TYPE_CHECKING: bool

class LineageBackend:
    def send_lineage(self, operator: BaseOperator, inlets: list | None = ..., outlets: list | None = ..., context: dict | None = ...): ...
