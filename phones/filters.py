import django_filters
from .models import Phone

class PhoneFilter(django_filters.FilterSet):
    # Price range filter (Min - Max)
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Phone
        fields = ['brand', 'ram', 'storage']