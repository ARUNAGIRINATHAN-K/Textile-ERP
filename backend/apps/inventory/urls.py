from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import InventoryItemViewSet, StockTransactionViewSet, InventoryAggregateViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='inventory-item')
router.register(r'transactions', StockTransactionViewSet, basename='stock-transaction')
router.register(r'aggregates', InventoryAggregateViewSet, basename='inventory-aggregate')

urlpatterns = [
    path('', include(router.urls)),
]
