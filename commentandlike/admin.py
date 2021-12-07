from django.contrib import admin

from .models import *

admin.site.register(Products_Likes)
admin.site.register(Products_Comments)
admin.site.register(Products_Comment_likes)
admin.site.register(Products_Comment_reply)

admin.site.register(Post_Likes)
admin.site.register(Post_Comments)
admin.site.register(Post_Comment_likes)
admin.site.register(Post_Comment_reply)

admin.site.register(Comment_for_customer)
admin.site.register(SendMessage)

# Register your models here.
