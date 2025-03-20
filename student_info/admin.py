from django.contrib import admin
from .models import student,student2,student3
# Register your models here.

class studentadmin(admin.ModelAdmin):
    ordering = ['rollno']  
    list_display = ("rollno" , "name" , "dob","photo")
    
class studentadmin2(admin.ModelAdmin):
    ordering = ['rollno']  
    list_display = ("rollno" , "name" , "dob","photo")
    
class studentadmin3(admin.ModelAdmin):
    ordering = ['rollno']  
    list_display = ("rollno" , "name" , "dob","photo")
    
admin.site.register(student, studentadmin)
admin.site.register(student2, studentadmin2)
admin.site.register(student3, studentadmin3)
