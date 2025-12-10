from __future__ import annotations

import json
from typing import Any, Tuple


def parse_json_field(raw: Any, field: str) -> Tuple[dict | None, str | None]:
    """Parse a JSON-like field that may be dict or string. Returns (dict_or_None, error_str_or_None)."""
    if raw is None or raw == "":
        return None, None
    if isinstance(raw, dict):
        return raw, None
    try:
        return json.loads(str(raw)), None
    except Exception as exc:  # noqa: BLE001
        return None, f"Invalid JSON for {field}: {exc}"

