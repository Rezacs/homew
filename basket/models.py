from django.db import models
from django.db.models.fields import IntegerField

from customer.models import *
from products.models import *
from django.contrib.auth import get_user_model

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

from django.contrib.auth import get_user_model

class Basket ( models.Model ) :
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [ 
        ('live' , 'live_basket_now'),
        ('past' , 'payed and cheked'),
        ('done' , 'finished basket'),
    ]
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES
    )
    address = models.ForeignKey( Address , on_delete=models.PROTECT , blank=True , null=True)
    price = models.PositiveIntegerField( blank=True, null=True)

    def calculate ( obj ) :
        sum = 0
        items = BasketItem.objects.filter(basket = obj )
        for item in items :
            sum += ( item.price * item.quantity )
        return sum

    def save(self , *args , **kwargs) :
        self.price = self.calculate()
        super(Shop,self).save(*args , **kwargs)

    def __str__(self) -> str:
        return f"{self.owner} factor on {self.order_date}"

class BasketItem ( models.Model ) :
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.product} factor {self.added_date}"

class Order ( models.Model ) :
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE , default=None)
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

class Email_response ( models.Model ) :
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    desc = models.TextField(blank=True , help_text="Enter a description for your selected prod.")
    date_sent = models.DateTimeField(auto_now_add=True)
    seller_response = models.CharField(max_length=300)
    buyer_response = models.CharField(max_length=300)
