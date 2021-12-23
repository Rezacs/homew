from django.shortcuts import render
from commentandlike.models import *
from customer.models import *
from products.models import *
from products.serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import *
from products.forms import *
from django.contrib import messages


@api_view(['GET'])
def products_list_2(request):

    products = Products.objects.all()

    serializer = ProductsListSerializer(products , many=True)

    return Response(data = serializer.data , status=200)


@api_view(['GET'])
def products_detail_2(request , input_id):

    products = Products.objects.get(id = input_id)

    serializer = PostSerializer(products)

    return Response(data = serializer.data , status=200)


#
@api_view(['GET'])
def products_likes(request , input_id):

    #post = Post.objects.get(id = input_id)
    product_like = Products_Likes.objects.filter(products__id = input_id )

    serializer = ProductsLikeSerializer(product_like)

    return Response(data = serializer.data , status=200)
#

@api_view(['GET'])
def post_comments_list_2(request):

    comments = Post_Comments.objects.all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

@api_view(['GET'])
def post_comments_detail_2(request , comment_id):

    comments = Post_Comments.objects.filter(id = comment_id).all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

#FINAL_PROJECT
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,ListView,DetailView



@login_required(login_url='login-mk')
def shop_dashboard ( request ) :
    user = request.user
    shops = Shop.not_deleted.filter(owner = user)
    customer = Customer.objects.get(user_name=user.username)
    followers = UserConnections.objects.filter(follower=user)
    followings = UserConnections.objects.filter(following=user)
    return render ( request , 'set_shop/dashboard.html' , {
        'shops' :shops,
        'user' : user,
        'customer':customer,
        'followers':followers,
        'followings':followings,
    })

@login_required(login_url='login-mk')
def add_Shop ( request ) :
    form = AddShopForm(request.POST or None )
    if request.method == "POST" :
        if form.is_valid() :
            # ['status' , 'owner' , 'customer' , 'admin_description' , 'created_on']
            shop = form.save(commit=False)
            shop.status = 'load'
            shop.owner = request.user
            shop.customer= Customer.objects.get(user_name = request.user.username)
            shop.save()
            messages.add_message(request, messages.SUCCESS, 'comment was saved !')
            return redirect(reverse('tag-list'))
    return render(request,'set_shop/shop_form.html' ,{
        'form' : form
    })

class ShopDetailView(DetailView):
    model = Shop
    # This file should exist somewhere to render your page
    template_name = 'set_shop/Shop_view.html'
    # Should match the value after ':' from url <slug:the_slug>
    # slug_url_kwarg = 'the_slug'
    # Should match the name of the slug field on the model 
    # slug_field = 'slug' # DetailView's default value: optional
    context_object_name = 'post'
