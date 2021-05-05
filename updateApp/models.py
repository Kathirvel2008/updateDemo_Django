from django.db import models

# Create your models here.

class Details(models.Model):
    user_name = models.CharField(max_length = 50)
    user_age = models.IntegerField()
    user_dob = models.DateField()

    user_id = models.IntegerField()
    user_city = models.CharField(max_length = 100)
    user_country = models.CharField(max_length = 100)
