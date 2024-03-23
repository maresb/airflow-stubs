import airflow.metrics.base_stats_logger
from airflow.configuration import conf as conf
from airflow.metrics.base_stats_logger import NoStatsLogger as NoStatsLogger
from typing import ClassVar

TYPE_CHECKING: bool

class _Stats(type):
    instance: ClassVar[None] = ...
    factory: ClassVar[type[airflow.metrics.base_stats_logger.NoStatsLogger]] = ...
    @classmethod
    def __getattr__(cls, name: str) -> str: ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_constant_tags(cls) -> list[str]: ...

class Stats:
    instance: ClassVar[airflow.metrics.base_stats_logger.NoStatsLogger] = ...
