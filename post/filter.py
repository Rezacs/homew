
import django_filters

from post.models import Post


class PostListFilterss(django_filters.FilterSet):
    # creator_isnull = django_filters.BoleanFilter(field_name='creator', lookup_expr='isnull')

    #title = django_filters.CharFilter(lookup_expr='icontains')
    # created = django_filters.NumberFilter(field_name='created', lookup_expr='year')
    # created1 = django_filters.NumberFilter(field_name='created', lookup_expr='year__gt')
    # created2 = django_filters.NumberFilter(field_name='created', lookup_expr='year__lt')

    class Meta:
        model = Post
        fields = ['title' , 'category' ]
        # fields = {
        #     'created_on': ['exact', 'year__gt' , 'month__lt'],
        #     'category' : ['exact']
        # }