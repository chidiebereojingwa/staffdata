from django.db import models

# Create your models here

class StaffData(models.Model):
    name = models.CharField(max_length=60, verbose_name='Staff Name')
    phone = models.IntegerField(verbose_name='Phone Number')
    email = models.EmailField(verbose_name='E-Mail')
    address = models.CharField(max_length=60, verbose_name='Address')

    def __str__(self):
        return self.name