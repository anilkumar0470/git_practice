import json
from django.shortcuts import render
from .models import Employee
from django.views import View
from django.http import HttpResponse
from django.core.serializers import serialize
from .forms import EmployeeForm


def blog_home(request):

    return HttpResponse("<h1>Blog home</h1>")

class CBVEmployee(View):

    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def get_object_by_id(self, id):
        try :
            emp = Employee.object.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_data = self.is_valid_json(data)

        if not valid_data:
            return HttpResponse(json.dumps({"msg": "data must be in json format only"}), content_type="application/json",status=400)
        actual_data  = json.loads(data)
        emp_id = actual_data.get("id", None)
        if emp_id:
            emp_out = self.get_object_by_id(emp_id)
            if not emp_out:
                return HttpResponse(json.dumps({"msg": "specified resource not found "}, content_type="application/json", status=400))
            json_data = serialize('json', [emp_out])
            return HttpResponse(json_data, content_type="application/json", status=200)
        actual_data = Employee.objects.all()
        json_data = serialize('json', actual_data)
        return HttpResponse(json_data, content_type="application/json", status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_data = self.is_valid_json(data)
        if not valid_data:
            return HttpResponse(json.dumps({"msg": "data must be in json format only"}, content_type="application/json",
                                           status=400))
        actual_data = json.loads(data)
        form = EmployeeForm(actual_data)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({"msg": "resource created successfully "}), content_type="application/json",
                                status = 200)
        if form.errors:
            return HttpResponse(form.errors, content_type="application/json", status=400)



