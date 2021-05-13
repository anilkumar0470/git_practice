from django import forms
from .models import Employee

#
# class EmployeeForm(forms.ModelForm):
#
#     def clean_esal(self):
#
#         input_salary = self.cleaned_data["esal"]
#         if input_salary < 5000:
#             raise forms.ValidationError("The minimum salary must be greater that 5000")
#         return input_salary
#
#     class Meta:
#         model = Employee
#         fields = "__all__"

from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    def clean_esal(self):
        input_salary = self.cleaned_data["esal"]
        if input_salary < 5000:
            raise forms.ValidationError("The minimum salary must be greater that 5000")
        return input_salary

    class Meta:
        model = Employee
        fields = "__all__"
