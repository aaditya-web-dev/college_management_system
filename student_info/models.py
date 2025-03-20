from django.db import models

# Create your models here.

class student(models.Model):
    photo = models.FileField(upload_to="student/" , max_length=255)
    name = models.CharField(max_length=255)
    rollno = models.IntegerField(primary_key='true')
    dob = models.DateField(null=True)
    year = models.CharField(null=True,max_length=255,default="1st year")
    
class student2(models.Model):
    photo = models.FileField(upload_to="student/" , max_length=255)
    name = models.CharField(max_length=255)
    rollno = models.IntegerField(primary_key='true')
    dob = models.DateField(null=True)
    year = models.CharField(null=True,max_length=255,default="2nd year")
    
class student3(models.Model):
    photo = models.FileField(upload_to="student/" , max_length=255)
    name = models.CharField(max_length=255)
    rollno = models.IntegerField(primary_key='true')
    dob = models.DateField(null=True)
    year = models.CharField(null=True,max_length=255,default="3rd year")