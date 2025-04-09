from _typeshed import Incomplete
from airflow.api_connexion.parameters import validate_istimezone as validate_istimezone
from airflow.api_connexion.schemas.role_and_permission_schema import RoleSchema as RoleSchema
from airflow.providers.fab.auth_manager.models import User as User
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class UserCollectionItemSchema(SQLAlchemySchema):
    class Meta:
        model = User
        dateformat: str
    first_name: Incomplete
    last_name: Incomplete
    username: Incomplete
    active: Incomplete
    email: Incomplete
    last_login: Incomplete
    login_count: Incomplete
    fail_login_count: Incomplete
    roles: Incomplete
    created_on: Incomplete
    changed_on: Incomplete

class UserSchema(UserCollectionItemSchema):
    password: Incomplete

class UserCollection(NamedTuple):
    users: list[User]
    total_entries: int

class UserCollectionSchema(Schema):
    users: Incomplete
    total_entries: Incomplete

user_collection_item_schema: Incomplete
user_schema: Incomplete
user_collection_schema: Incomplete
