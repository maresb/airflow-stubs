import airflow.auth.managers.models.base_user
import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.auth.managers.models.base_user import BaseUser as BaseUser
from typing import ClassVar

TYPE_CHECKING: bool

class Action(sqlalchemy.orm.decl_api.Model):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    name: Incomplete
    def __init__(self, **kwargs) -> None: ...

class Resource(sqlalchemy.orm.decl_api.Model):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    name: Incomplete
    def __eq__(self, other) -> bool: ...
    def __neq__(self, other): ...
    def __init__(self, **kwargs) -> None: ...

class Role(sqlalchemy.orm.decl_api.Model):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    name: Incomplete
    permissions: Incomplete
    user: Incomplete
    def __init__(self, **kwargs) -> None: ...

class Permission(sqlalchemy.orm.decl_api.Model):
    __tablename__: ClassVar[str] = ...
    __table_args__: ClassVar[tuple] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    action_id: Incomplete
    action: Incomplete
    resource_id: Incomplete
    resource: Incomplete
    role: Incomplete
    def __init__(self, **kwargs) -> None: ...

class User(sqlalchemy.orm.decl_api.Model, airflow.auth.managers.models.base_user.BaseUser):
    __tablename__: ClassVar[str] = ...
    _perms: ClassVar[None] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    username: Incomplete
    password: Incomplete
    active: Incomplete
    email: Incomplete
    last_login: Incomplete
    login_count: Incomplete
    fail_login_count: Incomplete
    roles: Incomplete
    created_on: Incomplete
    changed_on: Incomplete
    created_by_fk: Incomplete
    changed_by_fk: Incomplete
    created_by: Incomplete
    changed_by: Incomplete
    created: Incomplete
    changed: Incomplete
    @classmethod
    def get_user_id(cls): ...
    def get_id(self): ...
    def get_name(self) -> str: ...
    def get_full_name(self): ...
    def __init__(self, **kwargs) -> None: ...
    @property
    def is_authenticated(self): ...
    @property
    def is_active(self): ...
    @property
    def is_anonymous(self): ...
    @property
    def perms(self): ...

class RegisterUser(sqlalchemy.orm.decl_api.Model):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    first_name: Incomplete
    last_name: Incomplete
    username: Incomplete
    password: Incomplete
    email: Incomplete
    registration_date: Incomplete
    registration_hash: Incomplete
    def __init__(self, **kwargs) -> None: ...
def add_index_on_ab_user_username_postgres(table, conn, **kw): ...
def add_index_on_ab_register_user_username_postgres(table, conn, **kw): ...
