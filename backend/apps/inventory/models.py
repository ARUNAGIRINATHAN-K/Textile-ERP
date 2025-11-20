from django.db import models, transaction
from django.conf import settings
from apps.procurement.models import RawMaterial

class InventoryItem(models.Model):
    """
    Thin wrapper to reference a stock-managed item.
    If you already use procurement.RawMaterial as the canonical item,
    this model provides inventory-specific meta (like reorder rules).
    """
    raw_material = models.OneToOneField(RawMaterial, on_delete=models.CASCADE, related_name='inventory_item')
    min_level = models.FloatField(default=0.0)
    max_level = models.FloatField(default=0.0)
    reorder_point = models.FloatField(default=0.0)
    safety_stock = models.FloatField(default=0.0)

    def __str__(self):
        return f"Inventory for {self.raw_material.sku}"

class StockTransaction(models.Model):
    """
    Append-only transactions. Use positive quantity for receipts and negative for consumption.
    Keep audit trail.
    """
    TYPE_CHOICES = [
        ('receipt', 'Receipt'),        # from procurement PO
        ('consumption', 'Consumption'),# used in production
        ('adjustment', 'Adjustment'),  # manual adjustments
        ('transfer_in', 'Transfer In'),
        ('transfer_out', 'Transfer Out'),
        ('scrap', 'Scrap'),
    ]

    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='transactions')
    quantity = models.FloatField()  # positive or negative
    txn_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    reference = models.CharField(max_length=255, blank=True, help_text="Optional reference (PO number, WO id)")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.txn_type} {self.quantity} for {self.inventory_item.raw_material.sku}"

class InventoryAggregate(models.Model):
    """
    Cached / materialized current stock levels per InventoryItem.
    This is updated transactionally when StockTransaction is created.
    """
    inventory_item = models.OneToOneField(InventoryItem, on_delete=models.CASCADE, related_name='aggregate')
    quantity = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.inventory_item.raw_material.sku}: {self.quantity}"
