from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    ClientModelViewSet,
    WarehouseModelViewSet,
    ProductModelViewSet,
    ShipmentModelViewSet,
    logout_view
)

router = DefaultRouter()
router.register(r'clients', ClientModelViewSet)
router.register(r'warehouses', WarehouseModelViewSet)
router.register(r'products', ProductModelViewSet)
router.register(r'shipments', ShipmentModelViewSet)

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', include(router.urls)),
]
