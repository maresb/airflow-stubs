from _typeshed import Incomplete

__all__ = ['hookimpl']

hookimpl: Incomplete

class DefaultPolicy:
    @staticmethod
    def get_dagbag_import_timeout(dag_file_path: str): ...
    @staticmethod
    def get_airflow_context_vars(context): ...
