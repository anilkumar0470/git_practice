from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
import json
from .mixins import SerializeMixin
from .mixins import RenderHttpResponse
from .forms import EmployeeForm
from django.http import HttpResponse


def home(request):

    return render(request, 'index.html')




class EmployeeCRUDCBV(RenderHttpResponse, SerializeMixin,View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
            return emp
        except Employee.DoesNotExist:
            emp = None
            return emp

    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def get(self, request, *args, **kwargs):
        data = request.body
        print("333")
        import pdb
        # pdb.set_trace()
        if data:
            valid_json = self.is_valid_json(data)
            if not valid_json:
                json_data = {"msg": "data must beeee json only"}
                return HttpResponse(json_data, content_type='application/json', status=400)
            pdata = json.loads(data)
            emp_id = pdata.get("id", None)
            print("@@@@@ {}".format(emp_id))
            if emp_id is not None:
                emp = self.get_object_by_id(id=emp_id)
                print("Eere {}".format(emp))
                if emp is None:
                    json_data = json.dumps({"msg":"specified resource is not available"})
                    return HttpResponse(json_data, content_type='application/json')
                json_data = self.serialize([emp,])
                return HttpResponse(json_data, content_type='application/json')
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        if not self.is_valid_json(data):
            json_data = json.dumps({"msg" : "data must b44e in json only"})
            return self.render_to_httpresponse(json_data, status=401)

        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg": "resource created successfully"})
            return self.render_to_httpresponse(json_data)
        if form.erros:
            json_data = json.dumps(form.errors)
            return self.render_to_httpresponse(json_data, 401)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = self.is_valid_json(data)
        if not valid_json:
            json_data = {"msg": "data must be json only"}
            return HttpResponse(json_data, content_type='application/json', status=400)
        pdata = json.loads(data)
        emp_id = pdata.get("id", None)
        print("@@@@@ {}".format(emp_id))
        if emp_id is None:
            json_data = {"msg": "to perform update id is mandatory"}
            return HttpResponse(json_data, content_type='application/json', status=400)

        emp = self.get_object_by_id(id=emp_id)
        print("Eere {}".format(emp))
        if emp is None:
            print("3333")
            json_data = json.dumps({"msg": "specified resource is not available"})
            return HttpResponse(json_data, content_type='application/json', status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid:
            form.save(commit=True)
            json_data = json.dumps({"msg": "resource updated successfully"})
            return self.render_to_httpresponse(json_data)
        if form.erros:
            json_data = json.dumps(form.errors)
            return self.render_to_httpresponse(json_data, 401)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = self.is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data musttt be json only"})
            return HttpResponse(json_data, content_type='application/json', status=400)
        pdata = json.loads(data)
        emp_id = pdata.get("id", None)
        print("333@@@@@ {}".format(emp_id))
        if emp_id is not None:
            emp = self.get_object_by_id(id=emp_id)
            print("Eere {}".format(emp))
            if emp is None:
                json_data = json.dumps({"msg": "specified resource is not available"})
                return HttpResponse(json_data, content_type='application/json')
            status, deleted_item = emp.delete()
            if status == 1:
                print(status, deleted_item)
                json_data = json.dumps({"msg": "resource deleted successfully"})
                return self.render_to_httpresponse(json_data)
            else:
                json_data = json.dumps({"msg": "unable to delete please try  again"})
                return self.render_to_httpresponse(json_data)
        json_data = json.dumps({"msg": "to perform delete id is mandatory please provide the same"})
        return self.render_to_httpresponse(json_data)













class EmployeeDetailCBV(RenderHttpResponse, SerializeMixin, View):
    def is_valid_json(self, data):
        try:
            json.loads(data)
            valid = True
        except ValueError:
            valid = False
        return valid

    def get(self, request, id,  *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
             json_data = json.dumps({"msg" : "the requested resource not available"})
             return self.render_to_httpresponse(json_data, status=404)
        else:
            json_data = self.serialize([emp])
            return self.render_to_httpresponse(json_data)

    def put(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({"msg": "the requested resouece not available"})
            return self.render_to_httpresponse(json_data, status=404)
        data = request.body
        valid_json = self.is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data must be in json format only"})
            return self.render_to_httpresponse(json_data)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadd': emp.eadd
        }
        original_data.update(provided_data)
        form =  EmployeeForm(original_data, instance=emp)
        if form.is_valid:
            form.save(commit=True)
            json_data = json.dumps({"msg": "resource updated successfully"})
            return self.render_to_httpresponse(json_data)
        if form.erros:
            json_data = json.dumps(form.errors)
            return self.render_to_httpresponse(json_data, 401)

    def delete(self, request, id, *args, **kwargs):

        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({"msg": "the requested resouece not available"})
            return self.render_to_httpresponse(json_data, status=404)
        status, deleted_item = emp.delete()
        if status == 1:
            print(status,deleted_item)
            json_data = json.dumps({"msg": "resource deleted successfully"})
            return self.render_to_httpresponse(json_data)
        else:
            json_data = json.dumps({"msg":"unable to delete please try  again"})
            return self.render_to_httpresponse(json_data)





# class EmployeeListCBV(RenderHttpResponse, SerializeMixin, View):
#
#     def is_valid_json(self, data):
#         try:
#             json.loads(data)
#             valid = True
#         except ValueError:
#             valid = False
#         return valid
#
#     def get(self, request, *args, **kwargs):
#         qs = Employee.objects.all()
#         json_data = self.serialize(qs)
#         return self.render_to_httpresponse(json_data)
#
#     def post(self, request, *args, **kwargs):
#         data = request.body
#         if not self.is_valid_json(data):
#             json_data = json.dumps({"msg" : "data must be in json only"})
#             return self.render_to_httpresponse(json_data, status=401)
#
#         emp_data = json.loads(data)
#         form = EmployeeForm(emp_data)
#         if form.is_valid():
#             form.save()
#             json_data = json.dumps({"msg": "resource created successfully"})
#             return self.render_to_httpresponse(json_data)
#         if form.erros:
#             json_data = json.dumps(form.errors)
#             return self.render_to_httpresponse(json_data, 401)
