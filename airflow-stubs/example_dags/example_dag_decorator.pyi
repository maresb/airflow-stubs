import airflow.models.baseoperator
from airflow.decorators import task as task
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dag import dag as dag, example_dag as example_dag
from airflow.operators.email import EmailOperator as EmailOperator
from typing import ClassVar

TYPE_CHECKING: bool

class GetRequestOperator(airflow.models.baseoperator.BaseOperator):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, context: Context): ...
def example_dag_decorator(*args, **kwargs): ...
