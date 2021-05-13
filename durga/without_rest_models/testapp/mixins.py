import json
from django.core.serializers import serialize


class SerializeMixin(object):

    def serialize(self, queryset):
        json_data = serialize('json', queryset)
        p_data = json.loads(json_data)
        final_list = []
        for row in p_data:
            final_list.append(row['fields'])

        return json.dumps(final_list)


from django.http import HttpResponse


class HttpResponseMixin(object):


    def render_to_http_response(self, json_data, status_code=200):

        return HttpResponse(json_data, content_type="application/json", status=status_code)
