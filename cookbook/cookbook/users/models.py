from django.db import models
from django.core.validators import int_list_validator
# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=125)
    price = models.DecimalField(max_digits=10,max_length=10,decimal_places=False)

    description = models.TextField()

    release_date = models.DateField()






    def __str__(self):
        return self.name



