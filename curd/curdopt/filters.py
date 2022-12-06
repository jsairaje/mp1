import django_filters 
from .models import asset 
class assetfilter(django_filters.FilterSet):
    class Meta:
        model=asset  
        fields="__all__"