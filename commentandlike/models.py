from django.db import models
from customer.models import *
from products.models import *
from post.models import *
from django.contrib.auth import get_user_model

class CommonInfo(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE ,blank=True , null=True )
    created_on = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True )

    class Meta:
        abstract = True

class Products_Likes ( CommonInfo ,models.Model ) :
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.customer} {self.products}"

    class Meta :
        unique_together = [['customer' , 'products']]

class Products_Comments ( CommonInfo ,models.Model ) :
    body = models.TextField(max_length=300)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    title = models.CharField(max_length=300 , blank=True , null=True)
    parent = models.ForeignKey( 'self' , default=None , null=True , blank=True,on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.customer} {self.products}"

class Products_Comment_likes ( CommonInfo ,models.Model ) :
    comments = models.ForeignKey(Products_Comments, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now_add=True)

    class Meta :
        unique_together = [['customer' , 'comments']]

    def __str__(self) -> str:
        return f"{self.customer} {self.comments}"

class Products_Comment_reply ( CommonInfo ,models.Model ) :
    comments = models.ForeignKey(Products_Comments, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.customer} {self.comments}"

class Post_Likes ( CommonInfo ,models.Model ) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.customer} {self.post}"

    class Meta :
        unique_together = [['customer' , 'post']]

class Post_Comments ( CommonInfo ,models.Model ) :
    body = models.TextField(max_length=300)
    title = models.CharField(max_length=300 , blank=True , null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey( 'self' , default=None , null=True , blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.customer}-{self.post}-{self.title}"

class Post_Comment_likes ( CommonInfo ,models.Model ) :
    comments = models.ForeignKey(Post_Comments, on_delete=models.CASCADE)

    class Meta :
        unique_together = [['customer' , 'comments']]

    def __str__(self) -> str:
        return f"{self.customer} {self.comments}"

class Post_Comment_reply ( CommonInfo ,models.Model ) :
    comments = models.ForeignKey(Post_Comments, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.customer} {self.comments}"



class Comment_for_customer ( models.Model ) :
    body = models.CharField(max_length=300)
    customer_writer = models.ForeignKey(Customer,related_name='writer' , on_delete=models.CASCADE)
    customer_reciever = models.ForeignKey(Customer,related_name='reciever' , on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.customer_writer} {self.customer_reciever}"

class SendMessage(models.Model):
    writer = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True , related_name='writer' )
    created_on = models.DateTimeField(auto_now_add=True)
    reciever = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True , related_name='reciever' )
    body = models.TextField(max_length=300)
    title = models.CharField(max_length=300 , blank=True , null=True)

    def __str__(self) -> str:
        return f"{self.writer} {self.reciever} {self.title}"

class UserConnections(models.Model):
    following = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True , related_name='following' )
    created_on = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True , related_name='follower' )

    def __str__(self) -> str:
        return f"{self.following} --> {self.follower}"





