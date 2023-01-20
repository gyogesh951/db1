from django.db import models

# Create your models here.
class student(models.Model):
    student=models.CharField(max_length=100)
class student_name(models.Model):
    sno=models.IntegerField
    name=models.CharField
    age=models.IntegerField
