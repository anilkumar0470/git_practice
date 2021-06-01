from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id', 'eno', 'ename', 'esal', 'eadd']


admin.site.register(Employee, EmployeeAdmin)
