from django.db import models
from django.conf import settings

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=128, unique=True)
    unit = models.CharField(max_length=32, default='meter')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"

class PurchaseOrder(models.Model):
    STATUS = [('draft','Draft'),('ordered','Ordered'),('received','Received'),('cancelled','Cancelled')]
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='purchase_orders')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=STATUS, default='draft')
    expected_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"PO-{self.id} {self.supplier.name}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.PROTECT)
    quantity = models.FloatField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    received_quantity = models.FloatField(default=0.0)

    def line_total(self):
        return float(self.quantity) * float(self.unit_price)
