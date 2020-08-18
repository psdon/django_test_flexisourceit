from rest_framework import serializers

from .models import StockOwned


class BuySellStockSerializer(serializers.Serializer):
    """"Buy Sell Stock Serializer."""
    stock_symbol = serializers.CharField(max_length=48)
    quantity = serializers.IntegerField()


class StockOwnedSerializer(serializers.ModelSerializer):
    stock_symbol = serializers.ReadOnlyField(source='stock.name')
    price = serializers.ReadOnlyField(source='stock.price')
    total_value = serializers.SerializerMethodField()

    class Meta:
        model = StockOwned
        fields = ['stock_symbol', 'price', 'quantity', 'total_value']

    @staticmethod
    def get_total_value(obj):
        return obj.stock.price * obj.quantity
