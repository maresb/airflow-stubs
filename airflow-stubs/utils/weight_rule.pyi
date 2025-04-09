from enum import Enum

DB_SAFE_MINIMUM: int
DB_SAFE_MAXIMUM: int

def db_safe_priority(priority_weight: int) -> int: ...

class WeightRule(str, Enum):
    DOWNSTREAM = 'downstream'
    UPSTREAM = 'upstream'
    ABSOLUTE = 'absolute'
    @classmethod
    def is_valid(cls, weight_rule: str) -> bool: ...
    @classmethod
    def all_weight_rules(cls) -> set[str]: ...
