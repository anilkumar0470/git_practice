# if we are using mixin means it always extends object class directly.
from django.http import HttpResponse


class HttpResponseMixin(object):
    def render_to_http_response(self, data):
        return HttpResponse(data, content_type="application/json")

