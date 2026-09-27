import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


data = {
    "product": "Keyboard",
    "price": Decimal("129.99"),
}

# TODO: передать свой encoder правильным параметром
result = json.dumps(data, cls=DecimalEncoder)

restored = json.loads(result)

assert restored == {
    "product": "Keyboard",
    "price": "129.99",
}

# Ответ на доп вопрос, мне не нужно самому вызывать encoder.default(data["price"])
# Те json.dumos создает экземпляр нашего класса который мы передали в cls
# и начинает использщовать его  метод дефолт для сериализации, те в нашем случае,
# если  встречается тип данных Decimal или любой другой который мы опишем внутри
