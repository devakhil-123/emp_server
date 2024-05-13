from django.db import models

# Create your models here.
class empmodel(models.Model):
    emp_name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    dept=models.CharField(max_length=100)
    email=models.EmailField()
 
 
 
 