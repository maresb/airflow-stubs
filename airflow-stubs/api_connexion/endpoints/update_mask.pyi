from airflow.api_connexion.exceptions import BadRequest as BadRequest
from typing import Any, Mapping, Sequence

def extract_update_mask_data(update_mask: Sequence[str], non_update_fields: list[str], data: Mapping[str, Any]) -> Mapping[str, Any]: ...
