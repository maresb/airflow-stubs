from airflow.exceptions import AirflowBadRequest as AirflowBadRequest, PoolNotFound as PoolNotFound
from airflow.models.pool import Pool as Pool
from airflow.utils.session import provide_session as provide_session

TYPE_CHECKING: bool
NEW_SESSION: None
def get_pool(name, session: Session = ...): ...
def get_pools(session: Session = ...): ...
def create_pool(name, slots, description, session: Session = ...): ...
def delete_pool(name, session: Session = ...): ...
