from airflow.models.baseoperator import BaseOperator as BaseOperator

class LineageBackend:
    def send_lineage(self, operator: BaseOperator, inlets: list | None = None, outlets: list | None = None, context: dict | None = None): ...
