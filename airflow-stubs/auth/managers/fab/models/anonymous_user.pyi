import airflow.auth.managers.models.base_user
import flask_login.mixins
from _typeshed import Incomplete
from airflow.auth.managers.models.base_user import BaseUser as BaseUser
from typing import ClassVar

class AnonymousUser(flask_login.mixins.AnonymousUserMixin, airflow.auth.managers.models.base_user.BaseUser):
    _roles: ClassVar[set] = ...
    _perms: ClassVar[set] = ...
    roles: Incomplete
    @property
    def perms(self): ...
