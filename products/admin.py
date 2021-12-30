from django.contrib import admin
from django.utils.html import format_html


from .models import *

class ShopAdmin(admin.ModelAdmin) :
    list_display = ('name' , 'owner' , 'contact_number' , 'created_on' , 'desc'  , 'show_image' , 'status')
    list_filter = ( 'status' , 'created_on' )
    search_fields = ('name' , 'desc')
    date_hierarchy = ('created_on')

    #fields = (('title' , 'writer') , ('shortdesc' , 'status') , 'body')

    # fieldsets = (
    #     (None , {
    #         'fields' : (('writer' , 'title')  , 'shortdesc')
    #     }) ,
    #     ('Advanced options' , {
    #         'classes' : ('collapse',) , # wide
    #         'fields' : ('location_lat' , 'location_lng') ,
    #     }) ,
    # )
    #save_on_top = True

    # inlines = [
    #     CommentInLine
    # ]

    list_per_page = 100

    # @admin.display(empty_value='???' , description= 'title and desc')
    # def view_birth_date(self,obj) :
    #     # return f'{} + {}'
    #     #return obj.shortdesc 

    #     return format_html(
    #         '<span style="color : red ;"> {} - {} </span>' ,
    #         obj.title ,
    #         obj.shortdesc ,
    #     )


    @admin.display(empty_value='???' , description= 'show image')
    def show_image(self,obj) :
        if (obj.image) :
            print(obj.image.url)

            return format_html(
                '<img src="{}" width=50 height=50 />' ,
                obj.image.url ,
            )
        return '-'

    list_editable = ('status' , )

    @admin.action(description='Mark selected stores as verified')
    def make_verified(modeladmin, request, queryset):
        queryset.update(status='chek')

    actions = [make_verified]

class ProductAdmin(admin.ModelAdmin) :
    list_display = ('name' ,'desc', 'shop' , 'price','quantity' , 'show_image' , 'created_on')
    list_filter = ( 'price' , 'created_on' , 'shop' , 'category')
    search_fields = ('name' ,)
    date_hierarchy = ('created_on')

    list_per_page = 100

    @admin.display(empty_value='???' , description= 'show image')
    def show_image(self,obj) :
        if (obj.image) :
            print(obj.image.url)

            return format_html(
                '<img src="{}" width=50 height=50 />' ,
                obj.image.url ,
            )
        return '-'



admin.site.register(Products , ProductAdmin)
admin.site.register(Shop , ShopAdmin)

# Register your models here.
