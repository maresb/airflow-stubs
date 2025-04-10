from _typeshed import Incomplete
from marshmallow import Schema
from typing import NamedTuple

class ConfigOptionSchema(Schema):
    key: Incomplete
    value: Incomplete

class ConfigOption(NamedTuple):
    key: str
    value: str

class ConfigSectionSchema(Schema):
    name: Incomplete
    options: Incomplete

class ConfigSection(NamedTuple):
    name: str
    options: list[ConfigOption]

class ConfigSchema(Schema):
    sections: Incomplete

class Config(NamedTuple):
    sections: list[ConfigSection]

config_schema: Incomplete
