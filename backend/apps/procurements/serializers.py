from rest_framework import serializers
from .models import Supplier, RawMaterial, PurchaseOrder, PurchaseOrderItem

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    raw_material = RawMaterialSerializer(read_only=True)
    raw_material_id = serializers.PrimaryKeyRelatedField(queryset=RawMaterial.objects.all(), source='raw_material', write_only=True)

    class Meta:
        model = PurchaseOrderItem
        fields = ['id','raw_material','raw_material_id','quantity','unit_price','received_quantity']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id','supplier','created_by','created_at','status','expected_date','remarks','items']
        read_only_fields = ['created_by','created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        po = PurchaseOrder.objects.create(**validated_data)
        for item in items_data:
            PurchaseOrderItem.objects.create(purchase_order=po, **item)
        return po
