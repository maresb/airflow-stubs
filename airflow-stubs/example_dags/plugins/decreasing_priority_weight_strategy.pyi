from _typeshed import Incomplete
from airflow.models import TaskInstance as TaskInstance
from airflow.plugins_manager import AirflowPlugin as AirflowPlugin
from airflow.task.priority_strategy import PriorityWeightStrategy as PriorityWeightStrategy

class DecreasingPriorityStrategy(PriorityWeightStrategy):
    def get_weight(self, ti: TaskInstance): ...

class DecreasingPriorityWeightStrategyPlugin(AirflowPlugin):
    name: str
    priority_weight_strategies: Incomplete
