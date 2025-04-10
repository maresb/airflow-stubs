import typing
from airflow.configuration import conf as conf
from airflow.models.operator import Operator as Operator
from airflow.utils.context import Context as Context

class MultiprocessingStartMethodMixin: ...

class ResolveMixin:
    def iter_references(self) -> typing.Iterable[tuple[Operator, str]]: ...
    def resolve(self, context: Context, *, include_xcom: bool = True) -> typing.Any: ...
