from django.contrib import admin
from .models import InventoryItem, StockTransaction, InventoryAggregate
from apps.procurement.models import RawMaterial

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('raw_material', 'min_level', 'max_level', 'reorder_point', 'safety_stock')
    search_fields = ('raw_material__name','raw_material__sku')

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('inventory_item','txn_type','quantity','reference','created_by','created_at')
    list_filter = ('txn_type',)
    search_fields = ('inventory_item__raw_material__sku','reference')

@admin.register(InventoryAggregate)
class InventoryAggregateAdmin(admin.ModelAdmin):
    list_display = ('inventory_item','quantity','last_updated')
    search_fields = ('inventory_item__raw_material__sku',)
