from django.utils.simplejson import dumps, loads, JSONEncoder
from django.utils.functional import curry


class DjangoJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, QuerySet):
            return loads(serialize('json', obj))
        return JSONEncoder.default(self, obj)

dumps = curry(dumps, cls=DjangoJSONEncoder)
