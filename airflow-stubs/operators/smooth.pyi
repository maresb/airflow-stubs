from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.utils.context import Context as Context

class SmoothOperator(BaseOperator):
    ui_color: str
    yt_link: str
    def __init__(self, **kwargs) -> None: ...
    def execute(self, context: Context): ...
