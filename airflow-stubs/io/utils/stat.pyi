from _typeshed import Incomplete

class stat_result(dict):
    st_dev: Incomplete
    st_size: Incomplete
    st_gid: Incomplete
    st_uid: Incomplete
    st_ino: Incomplete
    st_nlink: Incomplete
    @property
    def st_mtime(self): ...
    @property
    def st_mode(self): ...
