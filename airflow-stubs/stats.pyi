from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.metrics.base_stats_logger import NoStatsLogger as NoStatsLogger, StatsLogger as StatsLogger
from typing import Callable

log: Incomplete

class _Stats(type):
    factory: Callable
    instance: StatsLogger | NoStatsLogger | None
    def __getattr__(cls, name: str) -> str: ...
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_constant_tags(cls) -> list[str]: ...

Stats: StatsLogger
