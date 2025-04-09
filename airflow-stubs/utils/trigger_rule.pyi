from enum import Enum

class TriggerRule(str, Enum):
    ALL_SUCCESS = 'all_success'
    ALL_FAILED = 'all_failed'
    ALL_DONE = 'all_done'
    ALL_DONE_SETUP_SUCCESS = 'all_done_setup_success'
    ONE_SUCCESS = 'one_success'
    ONE_FAILED = 'one_failed'
    ONE_DONE = 'one_done'
    NONE_FAILED = 'none_failed'
    NONE_FAILED_OR_SKIPPED = 'none_failed_or_skipped'
    NONE_SKIPPED = 'none_skipped'
    DUMMY = 'dummy'
    ALWAYS = 'always'
    NONE_FAILED_MIN_ONE_SUCCESS = 'none_failed_min_one_success'
    ALL_SKIPPED = 'all_skipped'
    @classmethod
    def is_valid(cls, trigger_rule: str) -> bool: ...
    @classmethod
    def all_triggers(cls) -> set[str]: ...
