from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InventoryItem, StockTransaction, InventoryAggregate
from .serializers import InventoryItemSerializer, StockTransactionSerializer, InventoryAggregateSerializer
from django.db import transaction

class IsProcurementOrInventory(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow users with inventory or procurement role or admin
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ('inventory','procurement','admin')

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.select_related('raw_material').all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsProcurementOrInventory]

    @action(detail=True, methods=['get'])
    def aggregate(self, request, pk=None):
        item = self.get_object()
        try:
            agg = item.aggregate
            serializer = InventoryAggregateSerializer(agg)
            return Response(serializer.data)
        except InventoryAggregate.DoesNotExist:
            return Response({'quantity': 0.0}, status=status.HTTP_200_OK)

class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.select_related('inventory_item__raw_material').all()
    serializer_class = StockTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsProcurementOrInventory]
    http_method_names = ['get','post','head','options']

    def get_queryset(self):
        qs = super().get_queryset().order_by('-created_at')
        # optional filters via query params
        sku = self.request.query_params.get('sku')
        if sku:
            qs = qs.filter(inventory_item__raw_material__sku=sku)
        return qs

    @action(detail=False, methods=['post'])
    def bulk_receive(self, request):
        """
        Accepts bulk receipt list:
        { "items":[ {"inventory_item": id, "quantity": 10, "reference": "PO-1"}, ... ] }
        """
        items = request.data.get('items', [])
        created = []
        errors = []
        for idx, it in enumerate(items):
            serializer = self.get_serializer(data={
                'inventory_item': it.get('inventory_item'),
                'quantity': float(it.get('quantity', 0)),
                'txn_type': 'receipt',
                'reference': it.get('reference',''),
                'notes': it.get('notes','')
            }, context={'request': request})
            if serializer.is_valid():
                tx = serializer.save()
                created.append(self.get_serializer(tx).data)
            else:
                errors.append({ 'index': idx, 'errors': serializer.errors })
        if errors:
            return Response({'created': created, 'errors': errors}, status=status.HTTP_207_MULTI_STATUS)
        return Response({'created': created}, status=status.HTTP_201_CREATED)

class InventoryAggregateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryAggregate.objects.select_related('inventory_item__raw_material').all()
    serializer_class = InventoryAggregateSerializer
    permission_classes = [permissions.IsAuthenticated, IsProcurementOrInventory]

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """
        Returns items where quantity <= reorder_point + safety_stock
        """
        aggs = self.get_queryset().filter(
            quantity__lte=models.F('inventory_item__reorder_point') + models.F('inventory_item__safety_stock')
        )
        serializer = self.get_serializer(aggs, many=True)
        return Response(serializer.data)
