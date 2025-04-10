import typing
from _typeshed import Incomplete
from airflow.models.mappedoperator import MappedOperator as MappedOperator
from airflow.serialization.serialized_objects import SerializedBaseOperator as SerializedBaseOperator
from marshmallow import Schema, fields
from marshmallow_oneofschema import OneOfSchema

class CronExpression(typing.NamedTuple):
    value: str

class TimeDeltaSchema(Schema):
    objectType: Incomplete
    days: Incomplete
    seconds: Incomplete
    microseconds: Incomplete
    def make_time_delta(self, data, **kwargs): ...

class RelativeDeltaSchema(Schema):
    objectType: Incomplete
    years: Incomplete
    months: Incomplete
    days: Incomplete
    leapdays: Incomplete
    hours: Incomplete
    minutes: Incomplete
    seconds: Incomplete
    microseconds: Incomplete
    year: Incomplete
    month: Incomplete
    day: Incomplete
    hour: Incomplete
    minute: Incomplete
    second: Incomplete
    microsecond: Incomplete
    def make_relative_delta(self, data, **kwargs): ...

class CronExpressionSchema(Schema):
    objectType: Incomplete
    value: Incomplete
    def make_cron_expression(self, data, **kwargs): ...

class ScheduleIntervalSchema(OneOfSchema):
    type_field: str
    type_schemas: Incomplete
    def get_obj_type(self, obj): ...

class ColorField(fields.String):
    validators: Incomplete
    def __init__(self, **metadata) -> None: ...

class WeightRuleField(fields.String): ...
class TimezoneField(fields.String): ...

class ClassReferenceSchema(Schema):
    module_path: Incomplete
    class_name: Incomplete

class JsonObjectField(fields.Field): ...
