import json
import sys
from django.http import HttpResponseNotAllowed

def method(method="GET"):
    def wrapper(view_func):
        async def wrapped(request, *args, **kwargs):
            if request.method != method:
                return HttpResponseNotAllowed([method])
            return await view_func(request, *args, **kwargs)
        return wrapped
    return wrapper
