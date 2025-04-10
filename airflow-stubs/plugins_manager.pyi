from _typeshed import Incomplete
from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.hooks.base import BaseHook as BaseHook
from airflow.lineage.hook import HookLineageReader as HookLineageReader
from airflow.listeners.listener import ListenerManager as ListenerManager
from airflow.task.priority_strategy import PriorityWeightStrategy as PriorityWeightStrategy, airflow_priority_weight_strategies as airflow_priority_weight_strategies
from airflow.timetables.base import Timetable as Timetable
from airflow.utils.entry_points import entry_points_with_dist as entry_points_with_dist
from airflow.utils.file import find_path_from_directory as find_path_from_directory
from airflow.utils.module_loading import import_string as import_string, qualname as qualname
from importlib import metadata
from types import ModuleType
from typing import Any, Iterable

log: Incomplete
import_errors: dict[str, str]
plugins: list[AirflowPlugin] | None
loaded_plugins: set[str]
registered_hooks: list[BaseHook] | None
macros_modules: list[Any] | None
executors_modules: list[Any] | None
admin_views: list[Any] | None
flask_blueprints: list[Any] | None
menu_links: list[Any] | None
flask_appbuilder_views: list[Any] | None
flask_appbuilder_menu_links: list[Any] | None
global_operator_extra_links: list[Any] | None
operator_extra_links: list[Any] | None
registered_operator_link_classes: dict[str, type] | None
registered_ti_dep_classes: dict[str, type] | None
timetable_classes: dict[str, type[Timetable]] | None
hook_lineage_reader_classes: list[type[HookLineageReader]] | None
priority_weight_strategy_classes: dict[str, type[PriorityWeightStrategy]] | None
PLUGINS_ATTRIBUTES_TO_DUMP: Incomplete

class AirflowPluginSource:
    def __html__(self) -> None: ...

class PluginsDirectorySource(AirflowPluginSource):
    path: Incomplete
    def __init__(self, path) -> None: ...
    def __html__(self): ...

class EntryPointSource(AirflowPluginSource):
    dist: Incomplete
    version: Incomplete
    entrypoint: Incomplete
    def __init__(self, entrypoint: metadata.EntryPoint, dist: metadata.Distribution) -> None: ...
    def __html__(self): ...

class AirflowPluginException(Exception): ...

class AirflowPlugin:
    name: str | None
    source: AirflowPluginSource | None
    hooks: list[Any]
    executors: list[Any]
    macros: list[Any]
    admin_views: list[Any]
    flask_blueprints: list[Any]
    menu_links: list[Any]
    appbuilder_views: list[Any]
    appbuilder_menu_items: list[Any]
    global_operator_extra_links: list[Any]
    operator_extra_links: list[Any]
    ti_deps: list[Any]
    timetables: list[type[Timetable]]
    listeners: list[ModuleType | object]
    hook_lineage_readers: list[type[HookLineageReader]]
    priority_weight_strategies: list[type[PriorityWeightStrategy]]
    @classmethod
    def validate(cls) -> None: ...
    @classmethod
    def on_load(cls, *args, **kwargs) -> None: ...

def is_valid_plugin(plugin_obj): ...
def register_plugin(plugin_instance) -> None: ...
def load_entrypoint_plugins() -> None: ...
def load_plugins_from_plugin_directory() -> None: ...
def load_providers_plugins() -> None: ...
def make_module(name: str, objects: list[Any]): ...
def ensure_plugins_loaded() -> None: ...
def initialize_web_ui_plugins() -> None: ...
def initialize_ti_deps_plugins() -> None: ...
def initialize_extra_operators_links_plugins() -> None: ...
def initialize_timetables_plugins() -> None: ...
def initialize_hook_lineage_readers_plugins() -> None: ...
def integrate_executor_plugins() -> None: ...
def integrate_macros_plugins() -> None: ...
def integrate_listener_plugins(listener_manager: ListenerManager) -> None: ...
def get_plugin_info(attrs_to_dump: Iterable[str] | None = None) -> list[dict[str, Any]]: ...
def initialize_priority_weight_strategy_plugins() -> None: ...
