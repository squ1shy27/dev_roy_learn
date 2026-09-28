
import json


def json_default(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj


data = {
    "name": "Alice",
    "roles": {"admin", "editor"},
}

result = json.dumps(data, default=json_default)
restored = json.loads(result)

assert restored["name"] == "Alice"
assert set(restored["roles"]) == {"admin", "editor"}