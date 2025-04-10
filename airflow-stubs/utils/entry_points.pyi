from _typeshed import Incomplete
from importlib import metadata
from typing import Iterator

log: Incomplete
EPnD = tuple[metadata.EntryPoint, metadata.Distribution]

def entry_points_with_dist(group: str) -> Iterator[EPnD]: ...
