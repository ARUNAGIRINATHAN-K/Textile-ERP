from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, RawMaterialViewSet, PurchaseOrderViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'raw-materials', RawMaterialViewSet, basename='rawmaterial')
router.register(r'purchase-orders', PurchaseOrderViewSet, basename='purchaseorder')

urlpatterns = [
    path('', include(router.urls)),
]
