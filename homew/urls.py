"""homew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView

from post.views import *

from django.conf import Settings, settings
from django.conf.urls.static import static
from products.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard ),
    path('admin/', admin.site.urls),
    path('class_today',class_today_time),
    path('class_detail_post/<int:post_id>',class_detail_post),
    path('class_first_template',class_first_template),
    path('class_post_detail/<int:post_id>',class_post_detail,name='class_detail'),
    path('class_category_detail/<int:category_id>',class_category_detail,name='class_category_detail'),
    path('class_post_list',class_post_list , name = 'class-post-list'),
    # path('about' , TemplateView)
    path('post-detail-view/<int:pk>/', PostDetailView.as_view()),
    path('class_category_list' , class_category_list , name='category-list'),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('posts/<str:given_slug>/', class_post_slug_view, name='show_post'),
    path('class_category_posts/<str:category_name>',class_category_posts),
    path('class_category_posts/class_post_detail/<int:post_id>',class_post_detail),
    # HW19
    path('post_list_2',PostListFilter.as_view() , name='seri_post_list'), 
    path('comment_create_get',DRF_Create_comment.as_view()),
    path('post_detail_2/<int:input_id>',post_detail_2, name='seri_post_detail'), #
    path('post_detail_HW18/<int:id>',post_detail_update_delete, name='seri_post_detail_HW18'),
    path('HW19/<int:id>',post_detail_update_delete, name='HW19'),
    path('post_urls/', include('post.urls')),
    path("class_category_posts/gslug/<str:given_slug>", class_post_slug_view , name='post-slug-view'),
    # path('maktab-view', MaktabView.as_view()),
    # path('maktab-list',ListPostView.as_view())
    path('accounts/', include('django.contrib.auth.urls')),
    path('post_comments_list_2',post_comments_list_2 , name='seri_comment_list'), #
    path('post_comments_list_3/<int:post_id>',post_comments_list_3 , name='seri_comment_list_3'),
    path('customer_list',customer_list , name='customer-list'),
    path('customer_detail/<str:username>',customer_detailed , name='customer-detail'),
    path('post_comments_detail_2/<int:comment_id>',post_comments_detail_2 , name='seri_comment_detail'), #
    path('dashboard' , dashboard, name='dashboard'),
    path('logout' , user_logout, name='logout'),
    path('products_likes/<int:input_id>', products_likes),
    path( 'users_list' ,user_list , name='user-list' ),
    path('user/<str:username>' , user_page, name='page-view'),
    path('contact_us' , contact_us , name='contact-us'),
    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #reset password
    path('password-reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    #following and follower
    path('follow/<str:username>',follow,name="follow"),
    path('followersandfollowings/<str:username>',followersandfollowings , name="followers-and-followings"),
    path('unfollow/<str:username>',unfollow,name="unfollow"),
    path('removefollower/<str:username>',removefollower,name="removefollower"),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
