from _typeshed import Incomplete
from airflow.providers.fab.auth_manager.models import Action as Action, Permission as Permission, Resource as Resource, Role as Role
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class ActionSchema(SQLAlchemySchema):
    class Meta:
        model = Action
    name: Incomplete

class ResourceSchema(SQLAlchemySchema):
    class Meta:
        model = Resource
    name: Incomplete

class ActionCollection(NamedTuple):
    actions: list[Action]
    total_entries: int

class ActionCollectionSchema(Schema):
    actions: Incomplete
    total_entries: Incomplete

class ActionResourceSchema(SQLAlchemySchema):
    class Meta:
        model = Permission
    action: Incomplete
    resource: Incomplete

class RoleSchema(SQLAlchemySchema):
    class Meta:
        model = Role
    name: Incomplete
    permissions: Incomplete

class RoleCollection(NamedTuple):
    roles: list[Role]
    total_entries: int

class RoleCollectionSchema(Schema):
    roles: Incomplete
    total_entries: Incomplete

role_schema: Incomplete
role_collection_schema: Incomplete
action_collection_schema: Incomplete
