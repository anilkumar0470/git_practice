import json
from django.shortcuts import render
from django.http import HttpResponse


def emp_data_view(request):
    emp_data = {
        "eno": 1,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "mumbai"
    }
    response = "<h1> Employee Number : {} <br>Employee Name :{}</h1>".format(emp_data['eno'], emp_data['ename'])
    return HttpResponse(response)


def emp_data_json_view(request):
    emp_data = {
        "eno": 1,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "mumbai"
    }
    json_data = json.dumps(emp_data)

    return HttpResponse(json_data, content_type='application/json')


from django.http import JsonResponse


def emp_data_json_view2(request):
    emp_data = {
        "eno": 1,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "mumbai"
    }
    return JsonResponse(emp_data)


from django.views.generic import View
from .mixins import HttpResponseMixin


class JsonCBV(HttpResponseMixin, View):
    # def get(self, request, *args, **kwargs):
    #     emp_data = {
    #         "eno": 1,
    #         "ename": "Sunny",
    #         "esal": 1000,
    #         "eadd": "mumbai"
    #     }
    #     return JsonResponse(emp_data)
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from get method"})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from post method"})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from put method"})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from delete method"})
        return self.render_to_http_response(json_data)
