from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.views.generic import View
import json
from django.core.serializers import serialize
from .forms import StudentForm
class StudentCRUDCBV(View):

    def new_serialize(self, qs):
            json_data = serialize('json', qs)
            p_data = json.loads(json_data)
            final_list = []
            for obj in p_data:
                final_list.append(obj['fields'])
            json_data = json.dumps(final_list)
            return json_data

    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False


    def get_object_by_id(self, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            student = None
        return student

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = self.is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data must be in json format .. please provide valid json"})
            return HttpResponse(json_data, content_type='application/json', status=400)
        p_data = json.loads(data)
        student_id = p_data.get("id", None)
        if student_id:
            std_id_info = self.get_object_by_id(student_id)
            if not std_id_info:
                return HttpResponse(json.dumps({"msg" : "no mathced record found for given id"}),
                                    content_type='application/json', status=400)
            json_data = self.new_serialize([std_id_info])
            return HttpResponse(json_data, content_type='application/json', status=200)
        all_students = Student.objects.all()
        json_data = self.new_serialize(all_students)
        return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = self.is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data must be in json format .. please provide valid json"})
            return HttpResponse(json_data, content_type='application/json', status=400)
        std_data = json.loads(data)
        form = StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({"msg":"resource inserted successfully"}),
                                content_type='application/json', status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json', status='400')

    def put(self, request, *args, **kwargs):
        data = request.body

