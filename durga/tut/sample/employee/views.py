from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.views.generic import View


class EmployeeDetailViewCBV(View):

    def post(self,  request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        print(request.method)
        if form.is_valid():
            name  = form.cleaned_data["name"]
            emp_id = form.cleaned_data['emp_id']
            add = form.cleaned_data["add"]
            mobile_number = form.cleaned_data['mobile_number']
            emp = Employee(name=name, emp_id=emp_id, address=add,mobile_number=mobile_number)
            emp.save()
            return redirect("junk-details")



    def get(self, request, *args, **kwargs):
        form = EmployeeForm()
        return render(request, 'employee/register.html', {'form': form})


