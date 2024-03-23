from typing import Operator as Operator

__all__ = ['Operator', 'needs_expansion']

def needs_expansion(task: AbstractOperator) -> TypeGuard[Operator]: ...

# Names in __all__ with no definition:
#   Operator
