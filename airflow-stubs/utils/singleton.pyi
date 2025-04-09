from typing import Generic, TypeVar

T = TypeVar('T')

class Singleton(type, Generic[T]):
    def __call__(cls, *args, **kwargs) -> T: ...
