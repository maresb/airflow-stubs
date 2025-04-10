import warnings
from collections.abc import Generator

def capture_with_reraise() -> Generator[list[warnings.WarningMessage], None, None]: ...
