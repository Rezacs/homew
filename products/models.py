from django.db import models
from customer.models import *
from grups.models import *
from django.db.models import Q
from django.contrib.auth import get_user_model
import datetime
from django.template.defaultfilters import slugify, title
from random import randint

class NotDeletedShops(models.Manager):
    def get_queryset(self):
        return super(NotDeletedShops , self).get_queryset().filter( Q(status ='chek') | Q(status='load') | Q(status='rejc') )

class AcceptedShops(models.Manager):
    def get_queryset(self):
        #return super(AcceptedShops , self).get_queryset().filter( status='check' )
        return super().get_queryset().filter(status='chek')

class Shop ( models.Model ) :
    STATUS_CHOICES = [ 
        ('chek' , 'verified'),
        ('load' , 'in progress'),
        ('rejc' , 'rejected'),
        ('dele' , 'deleted'),
    ]
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES , blank=True , null=True
    )

    name = models.CharField(max_length=300)
    owner = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True , unique=True)
    desc = models.TextField(max_length = 250, null = True, blank = True ,)
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE ,blank=True , null=True)
    category = models.ManyToManyField(Category,blank=True , null=True   )
    Address = models.TextField( blank=True , null=True)
    contact_number = models.TextField( blank=True , null=True)
    # created_at
    admin_description = models.TextField( blank=True , null=True)
    created_on = models.DateTimeField( auto_now_add=True)

    objects = models.Manager()
    not_deleted = NotDeletedShops()
    accepted = AcceptedShops()

    def slugg(self):
        time = str(datetime.datetime.now())
        trash = str(self.customer.user_name+'-Shop-'+self.name+time)
        return slugify(trash)
    def save(self , *args , **kwargs) :
        if self.slug == None :
            if Shop.objects.filter(name = self.name).exists() :
                extra = str(randint(1,1000))
                self.slug = self.slugg()+'-'+extra
            else :
                self.slug = self.slugg()
        super(Shop,self).save(*args , **kwargs)

    def __str__(self) -> str:
        return f'{self.owner} - {self.name}'

    class Meta :
        unique_together = [['owner' , 'name']]


class AvailableProduct(models.Manager):
    def get_queryset(self):
        return super(AvailableProduct , self).get_queryset().filter(quantity__gt=0)

class UnavailableProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__lte=0)

class Products ( models.Model ) :
    SHIPPMENT_CHOICES = [ 
        ('pey' , 'peyk_motori'),
        ('pos' , 'post'),
        ('dgp' , 'digikala_post'),
    ]
    name = models.CharField(max_length=300)
    # description
    desc = models.TextField()
    body = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=300)
    weight = models.TextField()
    # secondary_group = models.ForeignKey(Secondary_group, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE , blank=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE , blank=True , null=True)
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    tag = models.ManyToManyField(Tag )
    category = models.ManyToManyField(Category  )
    price = models.PositiveIntegerField( blank=True, null=True)
    created_on = models.DateTimeField( auto_now_add=True ,null=True,blank=True )

    shippment = models.CharField(
        max_length=3,
        choices=SHIPPMENT_CHOICES
    )
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True , unique=True)


    # different Model
    objects = models.Manager()
    Available = AvailableProduct()
    UNAvailable = UnavailableProduct()

    def __str__(self) -> str:
        return f'{self.shop} - {self.name}'

    class Meta :
        unique_together = [['shop' , 'name']]

    def slugg(self):
        time = str(datetime.datetime.now())
        trash = str(self.shop.name +'-'+self.name)
        return slugify(trash)

    def save(self , *args , **kwargs) :
        if self.slug == None :
            if Products.objects.filter(name = self.name).exists() :
                extra = str(randint(1,1000))
                self.slug = self.slugg()+'-'+extra
            else :
                self.slug = self.slugg()
        super(Products,self).save(*args , **kwargs)

