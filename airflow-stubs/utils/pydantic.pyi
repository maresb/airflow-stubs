from pydantic import BaseModel as BaseModel, ConfigDict as ConfigDict, PlainSerializer as PlainSerializer, PlainValidator as PlainValidator, ValidationInfo as ValidationInfo

def is_pydantic_2_installed() -> bool: ...

class BaseModel:
    def __init__(self, *args, **kwargs) -> None: ...

class ConfigDict:
    def __init__(self, *args, **kwargs) -> None: ...

class PlainSerializer:
    def __init__(self, *args, **kwargs) -> None: ...

class PlainValidator:
    def __init__(self, *args, **kwargs) -> None: ...

class ValidationInfo:
    def __init__(self, *args, **kwargs) -> None: ...
