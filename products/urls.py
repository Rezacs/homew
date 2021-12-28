from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *

# app_name = 'post' 

urlpatterns = [
    path('dashboard', shop_dashboard , name='shop-dashboard'),
    path('add_shop', add_Shop , name='Add_shop'),
    path('view_shop/<int:id>', shop_owner_view , name='View_shop'),
    path('delete_shop/<int:id>', delete_shop , name='Delete_shop'),
    path('edit_shop/<int:id>', edit_shop , name='Edit_shop'),
    path('add_product/<int:ids>', add_product , name='Add_product'),
    path('product_detail/<int:id>', class_product_detail , name='Detail_product'),
    path('delete_product_comment/<int:comment_id>',delete_product_comment,name="delete-product-comment"),
    path('edit_product/<int:id>', edit_product , name='Edit_product'),
    path('edit_product_comment/<int:comment_id>', edit_comment , name='Edit_product_comment'),
    path('Shop/<str:username>', shop_page_view , name='Shop_Page'),
    path('add_product_comment/<int:comment_id>', add_product_comment , name='Product-comment-reply'),
    path('add_product_basket/<int:id>', add_to_basket , name='Add-Product-To-Basket'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)