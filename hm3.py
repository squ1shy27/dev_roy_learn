
import json


# Ответ а вопрос до запуска скрипта
# hook вызовется 3 раза, потому, что у нас 3 ключа name
# в calls значения запишутя в порядке root, Alice, London
# Я ошибся пришлос разбирать, что параметр object_hook сначала создает более глубокие объекты те по сути он разбирает словарь и идет из глубины
calls = []


def hook(obj):
    # TODO: добавить значение obj.get("name") в calls
    # только если ключ "name" существует
    if obj.get("name") is not None:
        calls.append(obj.get("name"))
    return obj


text = """
{
    "name": "root",
    "user": {
        "name": "Alice",
        "address": {
            "name": "London"
        }
    }
}
"""

result = json.loads(text, object_hook=hook)

assert result["user"]["address"]["name"] == "London"

# TODO: сначала пойми содержимое calls
assert calls == ['London', 'Alice', 'root']
