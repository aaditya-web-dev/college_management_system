from django.urls import path
from . import views as v1
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('professor/', v1.professor,name="pro"),
    path("teacher/<int:id>/",v1.teachers,name='teacher'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
