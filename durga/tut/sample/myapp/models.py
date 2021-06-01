from django.db import models


class DreamReal(models.Model):
    website = models.CharField(max_length=30)
    mail = models.EmailField()
    name = models.CharField(max_length=45)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = 'dreamreal' # myapp_modelName.
