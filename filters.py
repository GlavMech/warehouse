import django_filters
from api.models import Product, Shipment

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Исключаем уже отгруженные продукты
        self.filters['id'].extra.update({
            'queryset': Product.objects.exclude(shipments__isnull=False)
        })