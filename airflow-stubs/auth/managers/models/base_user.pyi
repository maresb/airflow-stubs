import abc
from abc import abstractmethod

class BaseUser(metaclass=abc.ABCMeta):
    @property
    def is_active(self) -> bool: ...
    @abstractmethod
    def get_id(self) -> str: ...
    @abstractmethod
    def get_name(self) -> str: ...
