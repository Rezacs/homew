from django.db import models
from customer.models import *
from grups.models import *

class AvailableProduct(models.Manager):
    def get_queryset(self):
        return super(AvailableProduct , self).get_queryset().filter(supply=True)

class UnavailableProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(supply=False)

class Products ( models.Model ) :
    SHIPPMENT_CHOICES = [ 
        ('pey' , 'peyk_motori'),
        ('pos' , 'post'),
        ('dgp' , 'digikala_post'),
    ]
    name = models.CharField(max_length=300)
    # description
    desc = models.TextField()
    quantity = models.PositiveIntegerField()
    supply = models.BooleanField(default=True)
    size = models.CharField(max_length=300)
    weight = models.PositiveIntegerField()
    # secondary_group = models.ForeignKey(Secondary_group, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    shippment = models.CharField(
        max_length=3,
        choices=SHIPPMENT_CHOICES
    )
    date_added = models.DateTimeField(auto_now_add=True)

    # different Model
    objects = models.Manager()
    published = AvailableProduct()
    published2 = UnavailableProduct()

    def __str__(self) -> str:
        return self.name

    class Meta :
        unique_together = [['customer' , 'name']]

