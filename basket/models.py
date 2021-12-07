from django.db import models
from django.db.models.fields import IntegerField

from customer.models import *
from products.models import *

# class Basket ( models.Model ) :
#     products = models.ForeignKey(Products, on_delete=models.CASCADE)
#     # products2 = models.ManyToManyField(Products)
#     quantity = models.PositiveIntegerField()
#     # quantity = models.PositiveIntegerField() < Products.quantity
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta :
#         unique_together = [['customer' , 'products']]

#     def __str__(self) -> str:
#         return f"{self.customer} {self.products}"

# class Order ( models.Model ) :
#     baskets = models.ForeignKey(Basket, on_delete=models.CASCADE)
#     desc = models.TextField(blank=True , help_text="Enter a description for your selected prod.")
#     date_created = models.DateTimeField(auto_now_add=True)
#     shipping_date = models.DateTimeField()
#     SHIPPMENT_CHOICES = [ 
#         ('pey' , 'peyk_motori'),
#         ('pos' , 'post'),
#         ('dgp' , 'digikala_post'),
#     ]
#     shippment = models.CharField(
#         max_length=3,
#         choices=SHIPPMENT_CHOICES
#     )
#     def __str__(self) -> str:
#         return f"{self.baskets}"

# class Email_response ( models.Model ) :
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     desc = models.TextField(blank=True , help_text="Enter a description for your selected prod.")
#     date_sent = models.DateTimeField(auto_now_add=True)
#     seller_response = models.CharField(max_length=300)
#     buyer_response = models.CharField(max_length=300)


#--------------------------


class Basket2 ( models.Model ) :
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    SHIPPMENT_CHOICES = [ 
        ('pey' , 'peyk_motori'),
        ('pos' , 'post'),
        ('dgp' , 'digikala_post'),
    ]
    shippment = models.CharField(
        max_length=3,
        choices=SHIPPMENT_CHOICES
    )
    def __str__(self) -> str:
        return f"{self.customer} factor on {self.order_date}"

class Basket2Item ( models.Model ) :
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    Basket = models.ForeignKey(Basket2, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.product} factor on {self.order_date}"

class Order2 ( models.Model ) :
    baskets = models.ForeignKey(Basket2, on_delete=models.CASCADE , default=None)
    desc = models.TextField(blank=True , help_text="Enter a description for your selected prod.")
    date_created = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateTimeField()
    SHIPPMENT_CHOICES = [ 
        ('pey' , 'peyk_motori'),
        ('pos' , 'post'),
        ('dgp' , 'digikala_post'),
    ]
    shippment = models.CharField(
        max_length=3,
        choices=SHIPPMENT_CHOICES
    )
    def __str__(self) -> str:
        return f"{self.baskets}"

class Email_response2 ( models.Model ) :
    order = models.ForeignKey(Order2, on_delete=models.CASCADE)
    desc = models.TextField(blank=True , help_text="Enter a description for your selected prod.")
    date_sent = models.DateTimeField(auto_now_add=True)
    seller_response = models.CharField(max_length=300)
    buyer_response = models.CharField(max_length=300)
