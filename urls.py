from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('ssignin' , views.ssignin, name='ssignin'),
    path('fsignin' , views.fsignin, name='fsignin'),
    path('ssignup' , views.ssignup, name='ssignup'),
    path('fsignup' , views.fsignup, name='fsignup'),
    path('stu_pg' , views.stu_pg, name='stu_pg'),
    path('fac_pg' , views.fac_pg, name='fac_pg'),
    path('upload' , views.upload, name='upload'),
    path('upload_exam' , views.upload_exam, name='upload_exam'),
    path('exam_list' , views.exam_list, name='exam_list'),
   
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)