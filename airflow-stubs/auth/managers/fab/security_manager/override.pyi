import airflow.auth.managers.fab.models
import airflow.auth.managers.fab.views.permissions
import airflow.auth.managers.fab.views.roles_list
import airflow.auth.managers.fab.views.user
import airflow.auth.managers.fab.views.user_edit
import airflow.auth.managers.fab.views.user_stats
import airflow.security.permissions as permissions
import airflow.www.security_manager
import flask_appbuilder.security.registerviews
import flask_appbuilder.security.views
from _typeshed import Incomplete
from airflow.auth.managers.fab.models import Action as Action, Permission as Permission, RegisterUser as RegisterUser, Resource as Resource, Role as Role, User as User
from airflow.auth.managers.fab.models.anonymous_user import AnonymousUser as AnonymousUser
from airflow.auth.managers.fab.views.permissions import ActionModelView as ActionModelView, PermissionPairModelView as PermissionPairModelView, ResourceModelView as ResourceModelView
from airflow.auth.managers.fab.views.roles_list import CustomRoleModelView as CustomRoleModelView
from airflow.auth.managers.fab.views.user import CustomUserDBModelView as CustomUserDBModelView, CustomUserLDAPModelView as CustomUserLDAPModelView, CustomUserOAuthModelView as CustomUserOAuthModelView, CustomUserOIDModelView as CustomUserOIDModelView, CustomUserRemoteUserModelView as CustomUserRemoteUserModelView
from airflow.auth.managers.fab.views.user_edit import CustomResetMyPasswordView as CustomResetMyPasswordView, CustomResetPasswordView as CustomResetPasswordView, CustomUserInfoEditView as CustomUserInfoEditView
from airflow.auth.managers.fab.views.user_stats import CustomUserStatsChartView as CustomUserStatsChartView
from airflow.auth.managers.utils.fab import get_method_from_fab_action_map as get_method_from_fab_action_map
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from airflow.www.security_manager import AirflowSecurityManagerV2 as AirflowSecurityManagerV2
from airflow.www.session import AirflowDatabaseSessionInterface as AirflowDatabaseSessionInterface
from flask_login.login_manager import LoginManager
from typing import Any, Callable, ClassVar, Collection, Iterable, Sequence

TYPE_CHECKING: bool
AUTH_DB: int
AUTH_LDAP: int
AUTH_OAUTH: int
AUTH_OID: int
AUTH_REMOTE_USER: int
LOGMSG_ERR_SEC_ADD_REGISTER_USER: str
LOGMSG_ERR_SEC_AUTH_LDAP: str
LOGMSG_ERR_SEC_AUTH_LDAP_TLS: str
LOGMSG_WAR_SEC_LOGIN_FAILED: str
LOGMSG_WAR_SEC_NOLDAP_OBJ: str
MICROSOFT_KEY_SET_URL: str
EXISTING_ROLES: set
NEW_SESSION: None
MAX_NUM_DATABASE_USER_SESSIONS: int

class FabAirflowSecurityManagerOverride(airflow.www.security_manager.AirflowSecurityManagerV2):
    auth_view: ClassVar[None] = ...
    registeruser_view: ClassVar[None] = ...
    user_view: ClassVar[None] = ...
    user_model: ClassVar[type[airflow.auth.managers.fab.models.User]] = ...
    role_model: ClassVar[type[airflow.auth.managers.fab.models.Role]] = ...
    action_model: ClassVar[type[airflow.auth.managers.fab.models.Action]] = ...
    resource_model: ClassVar[type[airflow.auth.managers.fab.models.Resource]] = ...
    permission_model: ClassVar[type[airflow.auth.managers.fab.models.Permission]] = ...
    authdbview: ClassVar[type[flask_appbuilder.security.views.AuthDBView]] = ...
    authldapview: ClassVar[type[flask_appbuilder.security.views.AuthLDAPView]] = ...
    authoidview: ClassVar[type[flask_appbuilder.security.views.AuthOIDView]] = ...
    authoauthview: ClassVar[type[flask_appbuilder.security.views.AuthOAuthView]] = ...
    authremoteuserview: ClassVar[type[flask_appbuilder.security.views.AuthRemoteUserView]] = ...
    registeruserdbview: ClassVar[type[flask_appbuilder.security.registerviews.RegisterUserDBView]] = ...
    registeruseroidview: ClassVar[type[flask_appbuilder.security.registerviews.RegisterUserOIDView]] = ...
    registeruseroauthview: ClassVar[type[flask_appbuilder.security.registerviews.RegisterUserOAuthView]] = ...
    actionmodelview: ClassVar[type[airflow.auth.managers.fab.views.permissions.ActionModelView]] = ...
    permissionmodelview: ClassVar[type[airflow.auth.managers.fab.views.permissions.PermissionPairModelView]] = ...
    rolemodelview: ClassVar[type[airflow.auth.managers.fab.views.roles_list.CustomRoleModelView]] = ...
    registeruser_model: ClassVar[type[airflow.auth.managers.fab.models.RegisterUser]] = ...
    registerusermodelview: ClassVar[type[flask_appbuilder.security.views.RegisterUserModelView]] = ...
    resourcemodelview: ClassVar[type[airflow.auth.managers.fab.views.permissions.ResourceModelView]] = ...
    userdbmodelview: ClassVar[type[airflow.auth.managers.fab.views.user.CustomUserDBModelView]] = ...
    resetmypasswordview: ClassVar[type[airflow.auth.managers.fab.views.user_edit.CustomResetMyPasswordView]] = ...
    resetpasswordview: ClassVar[type[airflow.auth.managers.fab.views.user_edit.CustomResetPasswordView]] = ...
    userinfoeditview: ClassVar[type[airflow.auth.managers.fab.views.user_edit.CustomUserInfoEditView]] = ...
    userldapmodelview: ClassVar[type[airflow.auth.managers.fab.views.user.CustomUserLDAPModelView]] = ...
    useroauthmodelview: ClassVar[type[airflow.auth.managers.fab.views.user.CustomUserOAuthModelView]] = ...
    userremoteusermodelview: ClassVar[type[airflow.auth.managers.fab.views.user.CustomUserRemoteUserModelView]] = ...
    useroidmodelview: ClassVar[type[airflow.auth.managers.fab.views.user.CustomUserOIDModelView]] = ...
    userstatschartview: ClassVar[type[airflow.auth.managers.fab.views.user_stats.CustomUserStatsChartView]] = ...
    jwt_manager: ClassVar[None] = ...
    oid: ClassVar[None] = ...
    oauth: ClassVar[None] = ...
    oauth_user_info: ClassVar[None] = ...
    oauth_allow_list: ClassVar[dict] = ...
    DAG_RESOURCES: ClassVar[set] = ...
    VIEWER_PERMISSIONS: ClassVar[list] = ...
    USER_PERMISSIONS: ClassVar[list] = ...
    OP_PERMISSIONS: ClassVar[list] = ...
    ADMIN_PERMISSIONS: ClassVar[list] = ...
    ROLE_CONFIGS: ClassVar[list] = ...
    DAG_ACTIONS: ClassVar[set] = ...
    def __init__(self, appbuilder) -> None: ...
    def register_views(self): ...
    def create_login_manager(self) -> LoginManager: ...
    def create_jwt_manager(self): ...
    def reset_password(self, userid, password): ...
    def reset_user_sessions(self, user: User) -> None: ...
    def load_user_jwt(self, _jwt_header, jwt_data): ...
    def create_builtin_roles(self): ...
    def create_admin_standalone(self) -> tuple[str | None, str | None]: ...
    def create_db(self): ...
    def get_readable_dags(self, user) -> Iterable[DagModel]: ...
    def get_editable_dags(self, user) -> Iterable[DagModel]: ...
    def get_accessible_dags(self, *args, **kwargs) -> Iterable[DagModel]: ...
    def get_accessible_dag_ids(self, *args, **kwargs) -> set[str]: ...
    @staticmethod
    def get_readable_dag_ids(user: Incomplete | None = ...) -> set[str]: ...
    @staticmethod
    def get_editable_dag_ids(user: Incomplete | None = ...) -> set[str]: ...
    def can_access_some_dags(self, action: str, dag_id: str | None = ...) -> bool: ...
    def get_all_permissions(self) -> set[tuple[str, str]]: ...
    def create_dag_specific_permissions(self) -> None: ...
    def prefixed_dag_id(self, dag_id: str) -> str: ...
    def is_dag_resource(self, resource_name: str) -> bool: ...
    def sync_perm_for_dag(self, dag_id: str, access_control: dict[str, Collection[str]] | None = ...) -> None: ...
    def add_permissions_view(self, base_action_names, resource_name): ...
    def add_permissions_menu(self, resource_name): ...
    def security_cleanup(self, baseviews, menus): ...
    def sync_roles(self) -> None: ...
    def create_perm_vm_for_all_dag(self) -> None: ...
    def add_homepage_access_to_custom_roles(self) -> None: ...
    def update_admin_permission(self) -> None: ...
    def clean_perms(self) -> None: ...
    def permission_exists_in_one_or_more_roles(self, resource_name: str, action_name: str, role_ids: list[int]) -> bool: ...
    def perms_include_action(self, perms, action_name): ...
    def init_role(self, role_name, perms) -> None: ...
    def bulk_sync_roles(self, roles: Iterable[dict[str, Any]]) -> None: ...
    def sync_resource_permissions(self, perms: Iterable[tuple[str, str]] | None = ...) -> None: ...
    def update_role(self, role_id, name: str) -> Role | None: ...
    def add_role(self, name: str) -> Role: ...
    def find_role(self, name): ...
    def get_all_roles(self): ...
    def delete_role(self, role_name: str) -> None: ...
    def get_roles_from_keys(self, role_keys: list[str]) -> set[Role]: ...
    def get_public_role(self): ...
    def add_user(self, username, first_name, last_name, email, role, password: str = ..., hashed_password: str = ...): ...
    def load_user(self, user_id): ...
    def get_user_by_id(self, pk): ...
    def count_users(self): ...
    def add_register_user(self, username, first_name, last_name, email, password: str = ..., hashed_password: str = ...): ...
    def find_user(self, username: Incomplete | None = ..., email: Incomplete | None = ...): ...
    def find_register_user(self, registration_hash): ...
    def update_user(self, user): ...
    def del_register_user(self, register_user): ...
    def get_all_users(self): ...
    def update_user_auth_stat(self, user, success: bool = ...): ...
    def get_action(self, name: str) -> Action: ...
    def create_action(self, name): ...
    def delete_action(self, name: str) -> bool: ...
    def get_resource(self, name: str) -> Resource: ...
    def create_resource(self, name) -> Resource: ...
    def get_all_resources(self) -> list[Resource]: ...
    def delete_resource(self, name: str) -> bool: ...
    def get_permission(self, action_name: str, resource_name: str) -> Permission | None: ...
    def get_resource_permissions(self, resource: Resource) -> Permission: ...
    def create_permission(self, action_name, resource_name) -> Permission | None: ...
    def delete_permission(self, action_name: str, resource_name: str) -> None: ...
    def add_permission_to_role(self, role: Role, permission: Permission | None) -> None: ...
    def remove_permission_from_role(self, role: Role, permission: Permission) -> None: ...
    def get_oid_identity_url(self, provider_name: str) -> str | None: ...
    @staticmethod
    def get_user_roles(user: Incomplete | None = ...): ...
    def auth_user_ldap(self, username, password): ...
    def auth_user_db(self, username, password): ...
    def oauth_user_info_getter(self, func: Callable[[AirflowSecurityManagerV2, str, dict[str, Any] | None], dict[str, Any]]): ...
    def get_oauth_user_info(self, provider: str, resp: dict[str, Any]) -> dict[str, Any]: ...
    @staticmethod
    def oauth_token_getter(): ...
    def check_authorization(self, perms: Sequence[tuple[str, str]] | None = ..., dag_id: str | None = ...) -> bool: ...
    def set_oauth_session(self, provider, oauth_response): ...
    def get_oauth_token_key_name(self, provider): ...
    def get_oauth_token_secret_name(self, provider): ...
    def auth_user_oauth(self, userinfo): ...
    def auth_user_oid(self, email): ...
    def auth_user_remote_user(self, username): ...
    def get_user_menu_access(self, menu_names: list[str] | None = ...) -> set[str]: ...
    @staticmethod
    def ldap_extract_list(ldap_dict: dict[str, list[bytes]], field_name: str) -> list[str]: ...
    @staticmethod
    def ldap_extract(ldap_dict: dict[str, list[bytes]], field_name: str, fallback: str) -> str: ...
    def filter_roles_by_perm_with_action(self, action_name: str, role_ids: list[int]): ...
    @property
    def get_session(self): ...
    @property
    def auth_type(self): ...
    @property
    def is_auth_limited(self): ...
    @property
    def auth_rate_limit(self): ...
    @property
    def auth_role_public(self): ...
    @property
    def oauth_providers(self): ...
    @property
    def auth_ldap_tls_cacertdir(self): ...
    @property
    def auth_ldap_tls_cacertfile(self): ...
    @property
    def auth_ldap_tls_certfile(self): ...
    @property
    def auth_ldap_tls_keyfile(self): ...
    @property
    def auth_ldap_allow_self_signed(self): ...
    @property
    def auth_ldap_tls_demand(self): ...
    @property
    def auth_ldap_server(self): ...
    @property
    def auth_ldap_use_tls(self): ...
    @property
    def auth_ldap_bind_user(self): ...
    @property
    def auth_ldap_bind_password(self): ...
    @property
    def auth_ldap_search(self): ...
    @property
    def auth_ldap_search_filter(self): ...
    @property
    def auth_ldap_uid_field(self): ...
    @property
    def auth_ldap_firstname_field(self): ...
    @property
    def auth_ldap_lastname_field(self): ...
    @property
    def auth_ldap_email_field(self): ...
    @property
    def auth_ldap_append_domain(self): ...
    @property
    def auth_ldap_username_format(self): ...
    @property
    def auth_ldap_group_field(self): ...
    @property
    def auth_roles_mapping(self): ...
    @property
    def auth_user_registration_role_jmespath(self): ...
    @property
    def api_login_allow_multiple_providers(self): ...
    @property
    def auth_username_ci(self): ...
    @property
    def auth_ldap_bind_first(self): ...
    @property
    def openid_providers(self): ...
    @property
    def auth_type_provider_name(self): ...
    @property
    def auth_user_registration(self): ...
    @property
    def auth_user_registration_role(self): ...
    @property
    def auth_roles_sync_at_login(self): ...
    @property
    def auth_role_admin(self): ...
    @property
    def oauth_whitelists(self): ...
    @property
    def builtin_roles(self): ...
