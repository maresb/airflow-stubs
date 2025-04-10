from _typeshed import Incomplete
from marshmallow import Schema
from typing import NamedTuple

class LogsSchema(Schema):
    content: Incomplete
    continuation_token: Incomplete

class LogResponseObject(NamedTuple):
    content: str
    continuation_token: str | None

logs_schema: Incomplete
