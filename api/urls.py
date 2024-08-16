from rest_framework.routers import DefaultRouter

from api.views import ClientModelViewSet, WarehouseModelViewSet, ProductModelViewSet, ShipmentModelViewSet

router = DefaultRouter()
router.register('clients', ClientModelViewSet)
router.register('warehouse', WarehouseModelViewSet)
router.register('product', ProductModelViewSet)
router.register('shipment', ShipmentModelViewSet)



urlpatterns = [
    #path('logout/', views.logout_view, name='logout'),
]

urlpatterns.extend(router.urls)