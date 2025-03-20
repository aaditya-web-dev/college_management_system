from django.urls import path
from . import views as v1
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('student/', v1.student_detail , name = "student"),
    path('student2/', v1.student_detail2 , name = "student2"),
    path('student3/', v1.student_detail3 , name = "student3"),
    path("bca/",v1.bca,name='bca')
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
