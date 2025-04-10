from airflow.models.baseoperator import BaseOperator
from airflow.models.mappedoperator import MappedOperator

__all__ = ['Operator']

Operator = BaseOperator | MappedOperator
