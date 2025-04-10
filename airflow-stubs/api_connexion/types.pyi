from flask import Response
from typing import Any, Mapping, Sequence

APIResponse = Response | tuple[object, int] | Mapping[str, Any]
UpdateMask = Sequence[str] | None
