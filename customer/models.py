from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# class MyUserManager ( BaseUserManager ) :
#     def create_user ( self , mobile , password = None , **other_fields ) :
#         if not mobile :
#             raise ValueError ( 'Mobile is required .. !')
#         user = self.model(mobile = mobile , **other_fields )
#         user.set_password ( password )
#         user.save()

#     def create_superuser ( self , mobile , password=None , **other_fields ) :
#         other_fields.setdefault('is_staff' , True)
#         other_fields.setdefault('is_superuser' , True)
#         other_fields.setdefault('is_active' , True)

#         if other_fields.get('is_staff') is not True :
#             raise ValueError ('Superuser must have is_staff=True')
#         if other_fields.get('is_superuser') is not True :
#             raise ValueError ('Superuser must have is_superuser=True')
#         return self.create_user( mobile , password , **other_fields )


# class MyUser ( AbstractUser ) :
#     username = None
#     mobile = models.CharField(max_length=11 , unique=True)
#     otp = models.PositiveIntegerField(blank=True , null=True)
#     otp_created_time = models.DateTimeField(auto_now=True)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'mobile'

#     REQUIRED_FIELDS = []

#     backend = ''


# ------------------------------------------------------

class Customer ( models.Model ) :
    GENDER_CHOICES = [ 
        ('mal' , 'male'),
        ('fem' , 'female'),
        ('not' , 'notset'),
    ]
    THEME_CHOICES = [ 
        ('gre' , 'green'),
        ('pur' , 'purpule'),
        ('red' , 'red'),
        ('blu' , 'blue'),
    ]
    first_name = models.CharField(max_length=300 ,blank=True , null=True)
    last_name = models.CharField(max_length=300,blank=True , null=True)
    user_name = models.CharField(max_length=100 , unique=True )
    desc = models.TextField(blank=True , null=True)
    # country = models.CharField(max_length=300)
    # city = models.CharField(max_length=300)
    # street = models.CharField(max_length=300)
    # zip = models.PositiveIntegerField()
    phone = models.PositiveIntegerField(blank=True , null=True , unique=True)
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    gender = models.CharField(
        max_length=3,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    theme = models.CharField(
        max_length=3,
        choices=THEME_CHOICES,
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True , null=True)
    birthday = models.DateField(blank=True , null=True)

    class Meta:
        ordering = ['user_name']

    def __str__(self) -> str:
        return self.user_name

class Payment ( models.Model ) :
    # many to one
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    class Meta:
        ordering = ['customer']

class Address ( models.Model ) :
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150 , blank=True , null=True)
    alley = models.CharField(max_length=150 , blank=True , null=True)
    number = models.CharField(max_length=150 , blank=True , null=True)
    zip = models.CharField(max_length=150)
    desc = models.TextField(blank=True , null=True)
    created_on = models.DateTimeField( auto_now_add=True ,null=True,blank=True )

