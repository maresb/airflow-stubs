from _typeshed import Incomplete
from airflow import DAG as DAG
from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import AlreadyExists as AlreadyExists, BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.dag_schema import DAGCollection as DAGCollection, DAGCollectionSchema as DAGCollectionSchema, DAGDetailSchema as DAGDetailSchema, DAGSchema as DAGSchema, dag_schema as dag_schema, dags_collection_schema as dags_collection_schema
from airflow.api_connexion.types import APIResponse as APIResponse, UpdateMask as UpdateMask
from airflow.exceptions import AirflowException as AirflowException, DagNotFound as DagNotFound
from airflow.models.dag import DagModel as DagModel, DagTag as DagTag
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.www.decorators import action_logging as action_logging
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from sqlalchemy.orm import Session as Session
from typing import Collection

def get_dag(*, dag_id: str, fields: Collection[str] | None = None, session: Session = ...) -> APIResponse: ...
def get_dag_details(*, dag_id: str, fields: Collection[str] | None = None, session: Session = ...) -> APIResponse: ...
def get_dags(*, limit: int, offset: int = 0, tags: Collection[str] | None = None, dag_id_pattern: str | None = None, only_active: bool = True, paused: bool | None = None, order_by: str = 'dag_id', fields: Collection[str] | None = None, session: Session = ...) -> APIResponse: ...
def patch_dag(*, dag_id: str, update_mask: UpdateMask = None, session: Session = ...) -> APIResponse: ...
def patch_dags(limit, session, offset: int = 0, only_active: bool = True, tags: Incomplete | None = None, dag_id_pattern: Incomplete | None = None, update_mask: Incomplete | None = None): ...
def delete_dag(dag_id: str, session: Session = ...) -> APIResponse: ...
