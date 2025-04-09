from _typeshed import Incomplete
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dag import DAG as DAG

class AddOneOperator(BaseOperator):
    value: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def execute(self, context): ...

class SumItOperator(BaseOperator):
    template_fields: Incomplete
    values: Incomplete
    def __init__(self, values, **kwargs) -> None: ...
    def execute(self, context): ...

add_one_task: Incomplete
sum_it_task: Incomplete
