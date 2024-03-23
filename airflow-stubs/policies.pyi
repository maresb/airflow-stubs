from pluggy._hooks import hookimpl as hookimpl

__all__ = ['hookimpl']

class DefaultPolicy:
    @staticmethod
    def get_dagbag_import_timeout(dag_file_path: str): ...
    @staticmethod
    def get_airflow_context_vars(context): ...

# Names in __all__ with no definition:
#   hookimpl
