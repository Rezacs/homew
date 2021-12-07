# pip install - req

# from django.contrib.auth.models import User

from rest_framework import fields, serializers
from commentandlike.models import *

from post.models import Post
from customer.models import *
from products.models import *

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name']

class ProductsDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['user_name']

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Likes
        fields = '__all__'





# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name' , 'last_name' , 'user_name'] 

# class PostSerializer(serializers.ModelSerializer):
#     customer = AccountSerializer(read_only=True)
#     class Meta:
#         model = Post
#         fields = '__all__'
#         # fields = ['id' , 'title' , 'created']
#         # depth = 1

# class PostCommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post_Comments
#         fields = '__all__'




    


        