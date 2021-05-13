# import json
# from django.shortcuts import render
# from django.views.generic import View
# from .models import Employee
# from django.http import HttpResponse
# from django.core.serializers import serialize
# # Create your views here.
#
#
# class EmployeeDetailCBV(View):
#
#     def get(self, request, id,  *args, **kwargs):
#         emp = Employee.objects.get(id=id)
#         # emp_data = {
#         #     "eno": emp.eno,
#         #     "ename": emp.ename,
#         #     "esal": emp.esal,
#         #     "eadd": emp.eadd
#         # }
#         # json_data = json.dumps(emp_data)
#         # return HttpResponse(json_data, content_type="application/json")
#         # fields attribute is to filter the output, letsay we have 10 fields in the data out of which we need to show
#         # only five fields to the user than we will specify those fields in the fields attribute
#
#         json_data = serialize('json', [emp, ], fields=('eno', 'ename', 'eadd'))
#         return HttpResponse(json_data, content_type='application/json')


from .models import Employee
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin, HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeDetailsCBV(SerializeMixin,HttpResponseMixin, View):
    print("ssssssssssssss")
    print("sdddddddddddddddddd")

    def get_object_by_id(self, id):
        try :
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def is_valid_json(self, data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def get(self, request, id, *args, **kwargs):
        try :
            emp_data = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({"msg": "the requested resource {} is not found".format(id)})
            return self.render_to_http_response(json_data, 404)
        else:
            json_data = self.serialize([emp_data, ])
            return self.render_to_http_response(json_data)

    def put(self, request, id, *args, **kwargs):
        print(" i am in class22222222222222222222222222222222222222222")
        emp = self.get_object_by_id(id)
        if emp is None:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$44444")
            json_data = json.dumps({"msg": "specified resource does not exist, update not possible"})
            return  self.render_to_http_response(json_data, status_code=400)
        input_data = request.body
        valid_json = self.is_valid_json(input_data)
        if not valid_json:
            json_data = json.dumps({"msg": "data must be in json/dict only"})
            return self.render_to_http_response(json_data, status_code=400)
        original_data = {
            "eno": emp.eno,
            "ename": emp.ename,
            "esal": emp.esal,
            "eadd": emp.eadd
        }
        original_data.update(json.loads(input_data))
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg": "resource updated successfully"})
            return HttpResponse(json_data, content_type="application/json", status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status_code=400)

    def delete(self, request, id, *args, **kwargs):

        emp = self.get_object_by_id(id)
        if emp is None:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$44444")
            json_data = json.dumps({"msg": "specified resource does not exist, delete not possible"})
            return self.render_to_http_response(json_data, status_code=400)
        status, deleted_item = emp.delete()
        print(status, deleted_item)
        if status == 1:

            print("$$$$$$$$$$$$$$$$$$$$$$$$$44444")
            json_data = json.dumps({"msg": "resource deleted successfully !!!"})
            return self.render_to_http_response(json_data, status_code=200)
        json_data = json.dumps({"msg": "Unable to delete plz try again !!!"})
        return self.render_to_http_response(json_data)







from django.views.generic import View
from .models import Employee
from django.core.serializers import serialize
from django.http import HttpResponse
from testapp.mixins import SerializeMixin, HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# this is for skipping csrf token verification
from .utils import is_valid_json
from .forms import EmployeeForm


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):

    def get(self, request, *args, **kwargs):
        emp_data = Employee.objects.all()
        # qs = serialize('json', emp_data, fields=('eno', 'ename', 'eadd'))
        # import json
        # query_set = json.loads(qs)
        # new_emp_set = []
        # for key in query_set:
        #     new_emp_set.append(key['fields'])
        # for key in query_set:
        #     # print("ddd")
        #     import pdb
        #     # pdb.set_trace()
        #     if "model" and "pk" in key:
        #         key.pop("model")
        #         key.pop("pk")
        #         print("sss")
        json_data = self.serialize(emp_data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        print ("asssssssssssssssssssasssssssaww")
        # assigning user sent data to some variable to verify whether it is valid or not
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data format must be json only"})
            return self.render_to_http_response(json_data, 400)
        # json_data = {"msg": "sent data is valid json"}
        # return self.render_to_http_response(json.dumps(json_data), 200)

        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg" : "resource created successfully!"})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status_code=400)

        # json_data = json.dumps({"msg": "this for post method"})

        # return self.render_to_http_response(json_data)



# from django.views.generic import View
# from django.core.serializers import serialize
# from .models import Employee
#
#
# class EmployeeListCBV(View):
#
#     def get(self, *args, **kwargs):
#         query_set = Employee.objects.all()
#         json_data = serialize('json', query_set)
#         return HttpResponse(json_data, content_type="application/json")

import json
from django.views.generic import View
from django.http import HttpResponse
from .forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeListPostCBV(View):

    def is_valid_json(self, data):
        try:
            output = json.loads(data)
            return True
        except ValueError:
            return False

    def is_valid_json(self, data):

        try:
            p_data = json.loads(data)
            return True
        except ValueError:
            return False

    def post(self, request, *args, **kwargs):
        input_body = request.body
        if not self.is_valid_json(input_body):
            json_data = json.dumps({"msg": "data format must be in json/dict only"})
            return HttpResponse(json_data, content_type="application/json", status=400)
        input_data = json.loads(input_body)
        form = EmployeeForm(input_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg": "resource created successfully!!!"})
            return HttpResponse(json_data, content_type="application/json", status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type="application/json", status=400)


from django.views.generic import View
# from django.core.serializers import serialize
from .mixins import HttpResponseMixin, SerializeMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class EmployeeCRUDCBV(HttpResponseMixin, SerializeMixin, View):
    def is_valid_json(self, data):

        try:
            p_data = json.loads(data)
            return True
        except ValueError:
            return False

    def get_object_by_id(self, id):
        try :
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data format must be json only"})
            return self.render_to_http_response(json_data, 400)
        pdata = json.loads(data)
        id = pdata.get("id", None)
        if id:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg": "the requested resource {} is not found".format(id)})
                return self.render_to_http_response(json_data, 404)
            json_data = self.serialize([emp, ])
            return self.render_to_http_response(json_data, 200)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data, 200)

    def post(self, request, *args, **kwargs):
        input_body = request.body
        if not self.is_valid_json(input_body):
            json_data = json.dumps({"msg": "data format must be in json/dict only"})
            return HttpResponse(json_data, content_type="application/json", status=400)
        input_data = json.loads(input_body)
        form = EmployeeForm(input_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg": "resource created successfully!!!"})
            return HttpResponse(json_data, content_type="application/json", status=200)
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type="application/json", status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data format must be json only"})
            return self.render_to_http_response(json_data, 400)
        pdata = json.loads(data)
        id = pdata.get("id", None)
        if id is None:
            json_data = json.dumps({"msg": "To perform update resource id must be required..please provide the same!"})
            return self.render_to_http_response(json_data, 400)
        else:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg": "No resource with given id , update cant possible .."
                                               "please try with valid id".format(id)})
                return self.render_to_http_response(json_data, 404)
            original_data = {
                "eno": emp.eno,
                "ename": emp.ename,
                "esal": emp.esal,
                "eadd": emp.eadd
            }
            original_data.update(json.loads(data))
            form = EmployeeForm(original_data, instance=emp)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({"msg": "resource updated successfully"})
                return HttpResponse(json_data, content_type="application/json", status=200)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status_code=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_valid_json(data)
        if not valid_json:
            json_data = json.dumps({"msg": "data format must be json only"})
            return self.render_to_http_response(json_data, 400)
        pdata = json.loads(data)
        id = pdata.get("id", None)
        if id:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg": "the requested resource {} is not found".format(id)})
                return self.render_to_http_response(json_data, 404)
            status, deleted_item = emp.delete()
            print(status, deleted_item)
            if status == 1:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$44444")
                json_data = json.dumps({"msg": "resource deleted successfully !!!"})
                return self.render_to_http_response(json_data, status_code=200)
            json_data = json.dumps({"msg": "Unable to delete plz try again !!!"})
            return self.render_to_http_response(json_data)
        else:
            json_data = json.dumps({"msg": "to perform delete operation id is mandatory !!"})
            return self.render_to_http_response(json_data, status_code=400)












