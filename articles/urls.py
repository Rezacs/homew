from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('theme' , ShowTemplate.as_view()),
    path('index' , MainPageView.as_view()),
    path('detail/<int:pk>' , PostDetailView.as_view()),
    path('simple_form' , simple_form),
    path("get-name/" , views.get_name , name="post_new"),
    path('get_name_2/', get_name_2),
]