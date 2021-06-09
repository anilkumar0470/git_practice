from django.shortcuts import render, redirect
from .models import EmployeeDetails
from .form import EmployeeForm


def display_employee_details(request):

    qs = EmployeeDetails.objects.all()

    return render(request, 'employee/employee_detail.html', {"details": qs})


def add_employee(request):
    if request.method == "POST":
        userform = EmployeeForm(request.POST)
        if userform.is_valid():
            ename = userform.cleaned_data.get("ename")
            eid = userform.cleaned_data.get("eid")
            esal = userform.cleaned_data.get("esal")
            eadd = userform.cleaned_data.get("eadd")
            empl1 = EmployeeDetails(ename=ename, esal=esal, eid=eid, eadd=eadd)
            empl1.save()

            return redirect('employee-details')
    else:
        userform = EmployeeForm()
    return render(request, 'employee/registration.html', {"form": userform})

