from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.


def emp_data_view(request):
    emp_data = {
        "eno": 100,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "Mumbai",

    }
    resp = "<h1> Employee number: {} <br> Employee Name: {} <br> Employee salary: {} <br> Employee address: {}  </h1>".\
        format(emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eadd'])
    return HttpResponse(resp)


def emp_data_json_view(request):

    emp_data = {
        "eno": 100,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "Mumbai",

    }
    import json
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type="application/json")

from django.http import JsonResponse


def emp_data_json_view2(request):

    emp_data = {
        "eno": 100,
        "ename": "Sunny",
        "esal": 1000,
        "eadd": "Mumbai",

    }

    return JsonResponse(emp_data)

from django.views.generic import View


class jsonCBV(View):
    def get(self, request, *args, **kwargs):
        emp_data = {
            "eno": 100,
            "ename": "Sunny",
            "esal": 1000,
            "eadd": "Mumbai",

        }
        return JsonResponse(emp_data)

from django.views.generic import View
from django.http import HttpResponse


class jsonCBV2(View):

    def get(self, request, *args, **kwargs):
        print("rrrr")
        import json
        json_data = json.dumps({"msg": "this is from class based view"})
        return HttpResponse(json_data, content_type="application/json")

from django.views.generic import View
from django.http import HttpResponse
import  json
from testapp.mixins import HttpResponseMixin


class NewjsonCBV(HttpResponseMixin, View):

    def get(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from get method class based views"})
        return self.render_to_http_response(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from post method class based views"})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from put method class based views"})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"msg": "this is from delete method class based views"})
        return self.render_to_http_response(json_data)