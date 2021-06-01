from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=30)
    esal = serializers.FloatField()
    eadd = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)