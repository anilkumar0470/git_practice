import json
from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_valid_json
from django.http import HttpResponse
from .models import Student
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class StudentCRUDCBV(View):

    def serialize_func(self, queryset):
        json_data = serialize('json', queryset)
        p_data = json.loads(json_data)
        final_list = []
        for row in p_data:
            final_list.append(row['fields'])

        return json.dumps(final_list)

    def get_object_by_id(self, id):
        try:
            s = Student.objects.get(id=id)
        except Student.DoesNotExist:
            # Employee.DoesNotExist
            s = None
        return s

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({"msg": "data must in json/dict only"}), content_type="application/json",
                                status=400)
        input_data = json.loads(data)
        id = input_data.get("id", None)
        if id:
            std = self.get_object_by_id(id)
            if std is None:
                return HttpResponse(json.dumps({"msg": "specified resource id {} not found ".format(id)}),
                                    content_type="application/json", status=400)
            json_data = self.serialize_func([std, ])
            return HttpResponse(json.dumps(json_data), content_type="application/json", status=200)
        all_std = Student.objects.all()
        json_data = self.serialize_func(all_std)
        return HttpResponse(json.dumps(json_data), content_type="application/json", status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            return HttpResponse(json.dumps({"msg": "data must in json/dict only"}), content_type="application/json",
                                status=400)
        input_data = json.loads(data)




