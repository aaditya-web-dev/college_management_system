from django.shortcuts import render,redirect
from .models import teacher_detail
# Create your views here.
def professor(request):
    return render(request,"professor.html")

def teachers(request,id):
    member=teacher_detail.objects.filter(id1=id)
    data={'data':member}
    return render(request,'teacher.html',data)
    
        
        




    