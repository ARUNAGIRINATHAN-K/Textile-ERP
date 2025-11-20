from rest_framework import serializers
from .models import InventoryItem, StockTransaction, InventoryAggregate
from apps.procurement.serializers import RawMaterialSerializer
from apps.procurement.models import RawMaterial

class InventoryItemSerializer(serializers.ModelSerializer):
    raw_material = RawMaterialSerializer(read_only=True)
    raw_material_id = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all(), source='raw_material', write_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'raw_material', 'raw_material_id', 'min_level', 'max_level', 'reorder_point', 'safety_stock']

class StockTransactionSerializer(serializers.ModelSerializer):
    inventory_item = serializers.PrimaryKeyRelatedField(queryset=InventoryItem.objects.all())
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = StockTransaction
        fields = ['id','inventory_item','quantity','txn_type','reference','created_by','created_at','notes']
        read_only_fields = ['created_by','created_at']

    def validate(self, data):
        # Basic validation: consumption/transfer_out should not create negative aggregate below some threshold?
        return data

    def create(self, validated_data):
        """
        Create a transaction and update InventoryAggregate atomically.
        """
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        validated_data['created_by'] = user

        from .models import InventoryAggregate  # local import to avoid circular
        with transaction.atomic():
            tx = StockTransaction.objects.create(**validated_data)
            agg, created = InventoryAggregate.objects.select_for_update().get_or_create(
                inventory_item=tx.inventory_item,
                defaults={'quantity': 0.0}
            )
            agg.quantity = float(agg.quantity) + float(tx.quantity)
            agg.save()
        return tx

class InventoryAggregateSerializer(serializers.ModelSerializer):
    inventory_item = InventoryItemSerializer(read_only=True)

    class Meta:
        model = InventoryAggregate
        fields = ['inventory_item','quantity','last_updated']
