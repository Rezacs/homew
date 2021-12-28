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
    path('tags/', TagListView.as_view() , name='tag-list'),
    path('edit-tag/<int:tag_id>', edit_tag_form , name='edit-tag-list'),
    path('delete-tag/<int:tag_id>', delete_tag_form , name='delete-tag-mk'),
    path('add_comment/<int:comment_id>', add_comment , name='add-comment'),
    path('login' , login_maktab , name='login-mk'),
    path('register' , register_maktab, name='register-mk'),
    path('new_password' , set_new_password, name='new-pass-mk'),
    path('new_post' , add_new_post, name='new-post'),
    path('edit_category_name/<int:category_id>', edit_category_form , name='edit-category'),
    path('add_category', add_category_form , name='add-category'),
    path('delete_category/<int:category_id>', delete_category_form , name='delete-category'),
    path('edit_post/<int:post_id>', edit_post, name='edit-post'),
    path('delete_post/<int:post_id>', delete_post , name='delete-post'),
    path('search_post' , search_post_title , name = 'search-post' ),
    path('search_username' , search_username , name = 'search-username' ),
    path('delete_comment/<int:comment_id>',delete_comment,name="delete-comment"),
    path('delete_message/<int:message_id>',delete_message,name="delete-message"),
    path('edit_comment/<int:comment_id>',edit_comment,name="edit-comment"),
    path('personal_info' ,edit_personal_info ,name='edit-personal-info' ),
    path('trash_search_post' , searchPageView.as_view() , name = 'trash-search-post' ),
    path('trash_search_post/<slug:slug>/<int:number>' , searchPageView.as_view() , name = 'trash-search-user-post' ),
    path('drafteds' , drafted_posts , name = 'draft-posts' ),
    path('login_mobile' , login_mobile , name='login-mobile-mk'),
    path('login_email' , login_email , name='login-email-mk'),
    path('edit_username' , edit_personal_info_user ,name='edit-personal-info-user' ),
    path('send_message/<str:username>' , send_message ,name='send-message' ),
    path('notify_followers' , MyFormView.as_view() ,name='notify-followers' ),
    path('comment_like/<int:comment_id>' , comment_like ,name='comment-like' ),
    path('liked_posts' , Liked_Posts ,name='liked-posts' ),
    path('unlike/<int:post_id>' , unlike ,name='unlike' ),
    path('inbox' , inbox ,name='inbox' ),
    path('post_liked_details/<int:post_id>' , liked_details ,name='post_liked_details' ),
    #CW20
    path('HW20' , CW_ajax ,name='HW20' ),
    #HW19
    path('post/<int:id>/', PostDetailUpdateDeleteView.as_view(), name='post_detail'),
    path('post_create', PostListCreate.as_view(), name='post_create'),
    # 2 dey
    path('edit_category/<int:pk>', GeeksUpdateView.as_view(), name='edit_category'),
    #6 dey
    path('addresses' , addresses ,name='Addresses' ),
    path('new_address' , add_address ,name='New-Address' ),
    path('delete_address/<int:id>', delete_address , name='delete-address'),
    path('edit_address/<int:id>', edit_address , name='edit-address'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)