from django.contrib import admin
from .models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ["id", "username", "fname", "lname","salary", "emp_id", "email"]


admin.site.register(Employee)

