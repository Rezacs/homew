from django.db import models
from django.contrib.auth import get_user_model

# class Grups ( models.Model ) :
#     name = models.CharField(max_length=300 , unique=True)
#     desc = models.TextField()

#     def __str__(self) -> str:
#         return self.name

# class Secondary_group ( models.Model ) :
#     name = models.CharField(max_length=300 , unique=True)
#     desc = models.TextField()
#     groupp = models.ForeignKey(Grups, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.name

class Category ( models.Model ) :
    name = models.CharField(max_length=300 , unique=True , blank=True)
    created_on = models.DateTimeField( auto_now_add=True , blank=True , null=True)
    parent = models.ForeignKey( 'self' , default=None , null=True , blank=True,
                                related_name='nested_category' ,on_delete=models.CASCADE)
    desc = models.TextField(blank=True , null=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta :
        ordering = ['-created_on']

class Tag ( models.Model ) :
    name = models.CharField(max_length=300 , unique=True)
    desc = models.TextField()

    class Meta : 
        verbose_name_plural = "تگ ها "
        verbose_name = "تگ"
        db_table = 'tag'
        ordering = ['-name']   # random : ?  ; ascending : -

    def __str__(self) -> str:
        return self.name
