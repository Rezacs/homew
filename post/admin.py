from django.contrib import admin

from commentandlike.models import Post_Comments

from .models import *
from django.utils.html import format_html

class CommentInLine (admin.TabularInline) :
    model = Post_Comments

class PostAdmin(admin.ModelAdmin) :
    list_display = ('title' , 'writer' , 'created_on' , 'shortdesc' , 'view_birth_date' , 'show_image' , 'status')
    list_filter = ('title', 'shortdesc' , 'status' , 'created_on' , 'category')
    search_fields = ('title' , 'shortdesc')
    date_hierarchy = ('created_on')
    #fields = (('title' , 'writer') , ('shortdesc' , 'status') , 'body')
    fieldsets = (
        (None , {
            'fields' : (('writer' , 'title')  , 'shortdesc')
        }) ,
        ('Advanced options' , {
            'classes' : ('collapse',) , # wide
            'fields' : ('location_lat' , 'location_lng') ,
        }) ,
    )
    #save_on_top = True
    inlines = [
        CommentInLine
    ]
    list_per_page = 100
    @admin.display(empty_value='???' , description= 'title and desc')
    def view_birth_date(self,obj) :
        # return f'{} + {}'
        #return obj.shortdesc 

        return format_html(
            '<span style="color : red ;"> {} - {} </span>' ,
            obj.title ,
            obj.shortdesc ,
        )


    @admin.display(empty_value='???' , description= 'show image')
    def show_image(self,obj) :
        if (obj.image) :
            print(obj.image.url)

            return format_html(
                '<img src="{}" width=50 height=50 />' ,
                obj.image.url ,
            )
        return '-'

    #list_editable = ('shortdesc' , 'status')

    @admin.action(description='mark post as published')
    def make_published(modeladmin , request , queryset) :
        queryset.update(status='PUB')




admin.site.register(Post , PostAdmin)
admin.site.register(Story)
admin.site.register(FeatureStory)
admin.site.register(InfographicStory)
admin.site.register(GalleryStory)
# admin.site.register(CommonInfo)

# Register your models here.
