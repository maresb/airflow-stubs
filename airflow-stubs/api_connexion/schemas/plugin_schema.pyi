from _typeshed import Incomplete
from marshmallow import Schema
from typing import NamedTuple

class PluginSchema(Schema):
    name: Incomplete
    hooks: Incomplete
    executors: Incomplete
    macros: Incomplete
    flask_blueprints: Incomplete
    appbuilder_views: Incomplete
    appbuilder_menu_items: Incomplete
    global_operator_extra_links: Incomplete
    operator_extra_links: Incomplete
    source: Incomplete
    ti_deps: Incomplete
    listeners: Incomplete
    timetables: Incomplete

class PluginCollection(NamedTuple):
    plugins: list
    total_entries: int

class PluginCollectionSchema(Schema):
    plugins: Incomplete
    total_entries: Incomplete

plugin_schema: Incomplete
plugin_collection_schema: Incomplete
