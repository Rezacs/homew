from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from post.views import *

# app_name = 'post' 

urlpatterns = [
    path('get_name/', get_name , name='get_name_mk'),
    path('add_tag/', add_tag_form , name='tag_mk'),
    path('add_tag_2/', AddTagView.as_view() , name='tag_mk_2'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)