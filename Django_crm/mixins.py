from django.db import models

class infomixin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    contact_no = models.CharField(max_length=50)
    adress  = models.CharField(max_length=10000)

    class Meta:
        abstract = True
