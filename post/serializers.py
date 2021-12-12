# pip install - req

# from django.contrib.auth.models import User

from rest_framework import fields, serializers
from commentandlike.models import Post_Comments

from post.models import Post
from customer.models import *

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id' , 'title' , 'created']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name' , 'last_name' , 'user_name'] 

class PostSerializer(serializers.ModelSerializer):
    customer = AccountSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id' , 'title' , 'created']
        # depth = 1

class PostCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Comments
        fields = '__all__'

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['writer' , 'slug' , 'customer']




    


        