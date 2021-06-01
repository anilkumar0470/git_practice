import io
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse


class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        data = request.body # json
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)

        emp_id = p_data.get("id", None)
        if emp_id:
            emp_info = Employee.objects.get(id=emp_id)
            eserial_data  = EmployeeSerializer(emp_info)
            json_data = JSONRenderer().render(eserial_data.data)
            return HttpResponse(json_data, content_type='application/json')
        qs = Employee.objects.all()
        eserial_data = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(eserial_data.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):

        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        eserial = EmployeeSerializer(data=p_data)
        if eserial.is_valid():
            eserial.save()
            msg = {"msg": "resource created successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(eserial.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)


