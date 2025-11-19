class SalesOrder(models.Model):
    order_no = models.CharField(max_length=100, unique=True)
    customer_info = models.JSONField()
    order_date = models.DateField(auto_now_add=True)
    shipped_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    total_value = models.DecimalField(max_digits=12, decimal_places=2)

class Shipment(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=255)
    tracking_no = models.CharField(max_length=255, null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    delivered_date = models.DateField(null=True, blank=True)
    feedback_score = models.IntegerField(null=True, blank=True)
    feedback_notes = models.TextField(null=True, blank=True)
