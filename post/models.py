import datetime
from django.db import models
from django.utils.translation import activate
from customer.models import *
from grups.models import *
from django.template.defaultfilters import slugify, title
from random import randint
from django.contrib.auth import get_user_model


class PublishedPosts(models.Manager):
    def get_queryset(self):
        return super(PublishedPosts , self).get_queryset().filter(status='PUB')

class DraftPosts(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='DRF')


class CommonInfo(models.Model):
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    shortdesc = models.CharField( 'short description',max_length=255,null=True,blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # created_at
    created_on = models.DateTimeField( auto_now_add=True)

    class Meta:
        abstract = True

STORY_TYPES = (
    ('f', 'Feature'),
    ('i', 'Infographic'),
    ('g', 'Gallery'),
)

class Story(CommonInfo ,models.Model):

    type = models.CharField(max_length=1, choices=STORY_TYPES)

    link = models.URLField(blank=True, null=True)

class FeatureManager(models.Manager):
    def get_queryset(self):
        return super(FeatureManager, self).get_queryset().filter(
            type='f')

class InfographicManager(models.Manager):
    def get_queryset(self):
        return super(InfographicManager, self).get_queryset().filter(
            type='i')

class GalleryManager(models.Manager):
    def get_queryset(self):
        return super(GalleryManager, self).get_queryset().filter(
            type='g')

class FeatureStory(Story):
    objects = FeatureManager()
    class Meta:
        proxy = True

class InfographicStory(Story):
    objects = InfographicManager()
    class Meta:
        proxy = True

class GalleryStory(Story):
    objects = GalleryManager()
    class Meta:
        proxy = True


#--------------------


class Post(CommonInfo):
    # id = ?
    writer = models.ForeignKey(get_user_model() , on_delete=models.PROTECT , blank=True , null=True)
    STATUS_CHOICES = [
        ('PUB','publish'),
        ('DRF','draft'),
        ('DEL','delete'),
        ('NOT','notset'),
    ]
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    category = models.ManyToManyField(Category  ) # ,on_delete=models.SET_NULL
    slug = models.SlugField(max_length = 250, null = True, blank = True , unique=True) 

    location_lat = models.DecimalField(max_digits=50, decimal_places=2,null=True,blank=True)
    location_lng =  models.DecimalField(max_digits=50, decimal_places=2,null=True,blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
    )

    objects = models.Manager()
    published = PublishedPosts()
    drafted = DraftPosts()

    def slugg(self):
        time = str(datetime.datetime.now())
        trash = str(self.customer.user_name+'-'+self.title+time)
        return slugify(trash)
    def save(self , *args , **kwargs) :
        if self.slug == None :
            if Post.objects.filter(title = self.title).exists() :
                extra = str(randint(1,1000))
                self.slug = self.slugg()+'-'+extra
            else :
                self.slug = self.slugg()
        super(Post,self).save(*args , **kwargs)
        
    @property
    def post_name(self):
        return f"{self.title} - {self.shortdesc}"

    class Meta:
        ordering = ['-created_on']

    # def time_status(self,param1):
    #     # نمایش اینکه چند ساعت درست شده پست ؟ تمرین
    #     print('data',param1)
        
    #     return param1 

    def __str__(self):
        return self.title


