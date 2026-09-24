from decimal import Decimal
import json


class FromDecimal(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return {'__Decimal__':str(obj)}
        return json.JSONEncoder.default(self, obj)

def as_Decimal(dct):
    val = dct.get('__Decimal__')
    if val is not None:
        return Decimal(val)
    return dct

a = [Decimal('0.11'), Decimal('0.33'), Decimal('0.66'), [Decimal('0.33'), Decimal('0.33'), 5]]

a_json = json.dumps(a, cls=FromDecimal)
print(a_json)
b = json.loads(a_json, object_hook=as_Decimal)
print(b)
