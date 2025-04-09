from airflow.configuration import conf as conf
from airflow.security.permissions import RESOURCE_DOCS as RESOURCE_DOCS, RESOURCE_DOCS_MENU as RESOURCE_DOCS_MENU
from airflow.utils.docs import get_docs_url as get_docs_url

def init_appbuilder_links(app) -> None: ...
