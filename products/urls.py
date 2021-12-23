from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *

# app_name = 'post' 

urlpatterns = [
    path('dashboard', shop_dashboard , name='dashboard'),
    path('add_shop', add_Shop , name='Add_shop'),
    path('view_shop/<int:pk>', ShopDetailView.as_view() , name='View_shop'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)