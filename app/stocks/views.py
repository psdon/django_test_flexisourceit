from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import StockOwned
from .serializers import BuySellStockSerializer, StockOwnedSerializer
from .services import buy_stock, sell_stock


class BuyStockViewSet(viewsets.ViewSet):
    """"Buy Stock Endpoint."""

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def create(request):
        """POST method."""
        serializer = BuySellStockSerializer(data=request.data)
        if serializer.is_valid():
            stock = request.data.get('stock_symbol')
            quantity = request.data.get('quantity')
            result = buy_stock(request, name=stock, quantity=quantity)

            if result['status'] == "success":
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellStockViewSet(viewsets.ViewSet):
    """
    Sell Stock Endpoint.
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def create(request):
        """POST method."""

        serializer = BuySellStockSerializer(data=request.data)
        if serializer.is_valid():
            stock = request.data.get('stock_symbol')
            quantity = request.data.get('quantity')
            result = sell_stock(request, name=stock, quantity=quantity)

            if result['status'] == "success":
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockOwnedViewSet(viewsets.ViewSet):
    """Stock Information Endpoint."""

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """Get Stock List Information Owned by User.
        :return Dict(stock_symbol, price, quantity, total_value)
        """
        queryset = StockOwned.objects.filter(user=request.user).all()
        serializer = StockOwnedSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Get Stock Information Owned by User.
        :param pk: String Stock Symbol
        :return Dict(stock_symbol, price, quantity, total_value)
        """
        queryset = StockOwned.objects.filter(user=request.user).all()
        stock_owned = get_object_or_404(queryset, stock__name=pk)
        serializer = StockOwnedSerializer(stock_owned)
        return Response(serializer.data)
