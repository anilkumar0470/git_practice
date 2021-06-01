from django import forms


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=30)
    emp_id = forms.IntegerField()
    add = forms.CharField(max_length= 50)
    mobile_number = forms.IntegerField()