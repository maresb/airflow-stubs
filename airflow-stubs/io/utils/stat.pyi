S_IFDIR: int
S_IFLNK: int
S_IFREG: int

class stat_result(dict):
    @property
    def st_dev(self): ...
    @property
    def st_size(self): ...
    @property
    def st_gid(self): ...
    @property
    def st_uid(self): ...
    @property
    def st_ino(self): ...
    @property
    def st_nlink(self): ...
    @property
    def st_mtime(self): ...
    @property
    def st_mode(self): ...
