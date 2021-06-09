from django import forms


class EmployeeForm(forms.Form):
    ename = forms.CharField(max_length=30)
    eid = forms.IntegerField()
    esal = forms.FloatField()
    eadd = forms.CharField(max_length=30)

