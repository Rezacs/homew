from django.shortcuts import render
from commentandlike.models import *
from customer.models import *
from products.models import *
from products.serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import *

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
