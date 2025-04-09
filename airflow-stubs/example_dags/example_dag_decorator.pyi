from _typeshed import Incomplete
from airflow.decorators import dag as dag, task as task
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.operators.email import EmailOperator as EmailOperator
from airflow.utils.context import Context as Context

class GetRequestOperator(BaseOperator):
    url: Incomplete
    def __init__(self, *, url: str, **kwargs) -> None: ...
    def execute(self, context: Context): ...

def example_dag_decorator(email: str = 'example@example.com'): ...

example_dag: Incomplete
