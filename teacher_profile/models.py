from django.db import models

# Create your models here.
class teacher_detail(models.Model):
    id1=models.IntegerField(unique=True,null=False)
    name=models.CharField(max_length=35)
    about=models.CharField(max_length=300,default="a")
    Designation=models.CharField(max_length=35)
    subject=models.CharField(max_length=35)
    education=models.CharField(max_length=35)
    exp=models.CharField(max_length=35)
    image=models.ImageField(upload_to="staff/")
    
    def __str__(self):
        return self.name