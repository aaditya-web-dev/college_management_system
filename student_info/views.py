from django.shortcuts import render
from .models import student,student2,student3
# Create your views here.

def bca(request):
    return render (request,"bca.html")

def student_detail(request):
    Student = student.objects.all() 
    data = {"student" : Student}
    return render(request, "student.html", data)

def student_detail2(request):
    Student = student2.objects.all() 
    data = {"student" : Student}
    return render(request, "student2.html", data)

def student_detail3(request):
    Student = student3.objects.all() 
    data = {"student" : Student}
    return render(request, "student3.html", data)