# from django.test import TestCase

from products.models import *
from products.serializers import *



p1 = Products.objects.all()
ProductsDetailListSerializer(p1,many=True).data


# t1 = ProductsLikeSerializer()
# print(t1)