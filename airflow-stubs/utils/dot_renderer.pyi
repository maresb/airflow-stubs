import graphviz
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import TaskInstance as TaskInstance
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dag import DAG as DAG
from airflow.models.mappedoperator import MappedOperator as MappedOperator
from airflow.models.taskmixin import DependencyMixin as DependencyMixin
from airflow.serialization.dag_dependency import DagDependency as DagDependency
from airflow.utils.dag_edges import dag_edges as dag_edges
from airflow.utils.state import State as State
from airflow.utils.task_group import TaskGroup as TaskGroup

def render_dag_dependencies(deps: dict[str, list[DagDependency]]) -> graphviz.Digraph: ...
def render_dag(dag: DAG, tis: list[TaskInstance] | None = None) -> graphviz.Digraph: ...
