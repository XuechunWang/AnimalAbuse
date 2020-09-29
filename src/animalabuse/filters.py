#from django.contrib.auth.models import User

from .models import animalabuse
import django_filters

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    county = django_filters.CharFilter(field_name="county", lookup_expr='icontains')
    Offense = django_filters.CharFilter(field_name="Offense",lookup_expr='icontains')
    convictiondate = django_filters.NumberFilter(field_name="convictiondate", lookup_expr='year')
    class Meta:
        model = animalabuse
        fields = ['name', 'county', 'Offense', 'convictiondate']
