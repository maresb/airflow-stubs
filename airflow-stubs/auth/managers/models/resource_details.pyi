from dataclasses import dataclass
from enum import Enum

@dataclass
class ConfigurationDetails:
    section: str | None = ...

@dataclass
class ConnectionDetails:
    conn_id: str | None = ...

@dataclass
class DagDetails:
    id: str | None = ...

@dataclass
class DatasetDetails:
    uri: str | None = ...

@dataclass
class PoolDetails:
    name: str | None = ...

@dataclass
class VariableDetails:
    key: str | None = ...

class AccessView(Enum):
    CLUSTER_ACTIVITY = 'CLUSTER_ACTIVITY'
    DOCS = 'DOCS'
    IMPORT_ERRORS = 'IMPORT_ERRORS'
    JOBS = 'JOBS'
    PLUGINS = 'PLUGINS'
    PROVIDERS = 'PROVIDERS'
    TRIGGERS = 'TRIGGERS'
    WEBSITE = 'WEBSITE'

class DagAccessEntity(Enum):
    AUDIT_LOG = 'AUDIT_LOG'
    CODE = 'CODE'
    DEPENDENCIES = 'DEPENDENCIES'
    RUN = 'RUN'
    SLA_MISS = 'SLA_MISS'
    TASK = 'TASK'
    TASK_INSTANCE = 'TASK_INSTANCE'
    TASK_RESCHEDULE = 'TASK_RESCHEDULE'
    TASK_LOGS = 'TASK_LOGS'
    WARNING = 'WARNING'
    XCOM = 'XCOM'
