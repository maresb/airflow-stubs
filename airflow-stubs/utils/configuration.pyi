from airflow.configuration import conf as conf
from airflow.utils.platform import IS_WINDOWS as IS_WINDOWS

def tmp_configuration_copy(chmod: int = 384, include_env: bool = True, include_cmds: bool = True): ...
